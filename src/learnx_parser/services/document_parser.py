import os
import shutil

from lxml import etree

from learnx_parser.models.core import PresentationDefaults, Slide
from learnx_parser.models.presentation import Presentation
from learnx_parser.parsers.presentation import PresentationParser
from learnx_parser.parsers.slide.base import SlideParser
from learnx_parser.services.background_renderer import BackgroundRenderer
from learnx_parser.services.style_resolver import StyleResolver
from learnx_parser.writers.html_writer import HtmlWriter
from learnx_parser.writers.json_writer import JsonWriter


class DocumentParser:
    def __init__(self, pptx_unpacked_path, output_dir="./output"):
        # Path to the unpacked PowerPoint presentation directory
        self.pptx_unpacked_path = pptx_unpacked_path
        # Directory where the generated HTML and JSON output will be saved
        self.output_dir = output_dir

        # Construct the path to the main presentation XML file
        self.presentation_xml_path = os.path.join(
            self.pptx_unpacked_path, "ppt", "presentation.xml"
        )
        # Initialize the PresentationParser to extract presentation-level data (e.g., slide order, slide size)
        self.presentation_parser = PresentationParser(self.presentation_xml_path)
        # Initialize the HtmlWriter for generating HTML output for each slide using absolute positioning
        self.html_writer = HtmlWriter(
            output_directory=self.output_dir,
            pptx_unpacked_path=self.pptx_unpacked_path,
        )
        # Initialize the JsonWriter for generating JSON output for each slide
        self.json_writer = JsonWriter(output_directory=self.output_dir)

    def _copy_media_for_slide(self, slide: Slide, slide_number: int):
        # Construct the output directory for media files specific to this slide
        media_output_directory = os.path.join(
            self.output_dir, f"slide{slide_number}", "media"
        )
        # Create the media output directory if it doesn't exist
        os.makedirs(media_output_directory, exist_ok=True)

        # Iterate through each picture in the slide data
        for picture in slide.pictures:
            # Check if the picture has associated blip fill data (which contains the image path)
            if picture.blip_fill:
                # Construct the original path of the media file within the unpacked PPTX
                media_relative_path = picture.blip_fill.path.lstrip("/").replace(
                    "../", ""
                )

                # Ensure the path includes 'ppt/' prefix for consistent handling
                # Some PPTX files have relative paths like "../media/image1.jpg" while others have "/ppt/media/image1.jpg"
                if not media_relative_path.startswith("ppt/"):
                    media_relative_path = "ppt/" + media_relative_path

                original_media_path = os.path.join(
                    self.pptx_unpacked_path, media_relative_path
                )
                # Construct the destination path for the media file in the output directory
                destination_media_path = os.path.join(
                    media_output_directory, os.path.basename(picture.blip_fill.path)
                )

                # Copy the media file if it exists at the original path
                if os.path.exists(original_media_path):
                    shutil.copy(original_media_path, destination_media_path)
                else:
                    # Print a warning if the media file is not found
                    print(f"Warning: Media file not found: {original_media_path}")

    def _get_slide_paths_and_rels(self):
        # Get the ordered list of slide relationship IDs from the presentation parser
        slide_r_ids = self.presentation_parser.get_slide_order()

        # Construct the path to the main presentation's relationship file
        presentation_relationships_path = os.path.join(
            self.pptx_unpacked_path, "ppt", "_rels", "presentation.xml.rels"
        )
        # Parse the relationships XML tree
        relationships_tree = etree.parse(presentation_relationships_path)
        # Initialize a dictionary to store presentation-level relationships (r:id to target path)
        presentation_relationships = {}
        # Iterate through each Relationship element in the relationships XML
        for relationship_element in relationships_tree.findall(".//{*}Relationship"):
            # Store the relationship ID and its target path
            presentation_relationships[relationship_element.get("Id")] = (
                relationship_element.get("Target")
            )

        slide_paths = []
        # Iterate through each slide relationship ID to resolve its actual file paths
        for r_id in slide_r_ids:
            # Get the target path for the current slide relationship ID
            slide_target = presentation_relationships.get(r_id)
            # If the target path cannot be resolved, print a warning and skip to the next slide
            if slide_target is None:
                print(f"Warning: Could not resolve slide r:id {r_id}")
                continue

            # Remove leading '/' if present, and replace '../' for relative paths to construct a clean relative path
            slide_xml_relative_path = slide_target.lstrip("/").replace("../", "")

            # Ensure the path includes 'ppt/' prefix for consistent handling
            # Some PPTX files have relative paths like "slides/slide1.xml" while others have "/ppt/slides/slide1.xml"
            if not slide_xml_relative_path.startswith("ppt/"):
                slide_xml_relative_path = "ppt/" + slide_xml_relative_path

            # Construct the absolute path to the slide's XML file
            slide_xml_path = os.path.join(
                self.pptx_unpacked_path, slide_xml_relative_path
            )

            # Extract the directory and base name of the slide XML file
            slide_directory = os.path.dirname(slide_xml_path)
            slide_name = os.path.basename(slide_xml_path)
            # Construct the absolute path to the slide's relationship file
            slide_relationships_path = os.path.join(
                slide_directory, "_rels", slide_name + ".rels"
            )

            # Check if the slide XML file exists; if not, print a warning and skip
            if not os.path.exists(slide_xml_path):
                print(f"Warning: Slide XML not found: {slide_xml_path}")
                continue
            # Check if the slide relationships file exists; if not, print a warning and set path to None
            # Some slides might not have a rels file if they don't link to anything
            if not os.path.exists(slide_relationships_path):
                print(
                    f"Warning: Slide relationships not found: {slide_relationships_path}"
                )
                slide_relationships_path = None

            # Append the resolved slide XML path and its relationships path to the list
            slide_paths.append((slide_xml_path, slide_relationships_path))
        return slide_paths

    def _generate_background_for_slide(self, slide: Slide, slide_number: int) -> str | None:
        """Generate background image for a slide using Goal 1: Background as Single Image.
        
        This method implements the core workflow for Goal 1 by checking if a slide has
        background properties and generating a PNG image if needed. The generated image
        path is then set on the slide object for HTML writer integration.
        
        The method checks for three types of background properties:
        1. background_color: Direct hex color values
        2. background_gradient_fill: Gradient definitions with color stops
        3. background_reference: Theme-based background references
        
        If any background properties are found, a PNG image is generated at
        1280×720 resolution and saved to the slide's media directory with the
        filename pattern "background_{slide_number}.png".
        
        Args:
            slide (Slide): Slide object containing common_slide_data with background properties
            slide_number (int): 1-based slide number used for filename generation
            
        Returns:
            str | None: Relative path to generated background image (e.g., "media/background_1.png")
                if background properties exist and image generation succeeds, None otherwise.
                
        Note:
            This method automatically creates the media output directory if it doesn't exist.
            The returned path is relative to the slide's output directory for HTML usage.
        """
        # Check if slide has any background properties
        has_background = (
            slide.common_slide_data.background_color or
            slide.common_slide_data.background_gradient_fill or
            slide.common_slide_data.background_reference or
            slide.common_slide_data.background_image_path
        )
        
        if not has_background:
            return None
        
        # Create the media output directory for this slide
        media_output_directory = os.path.join(
            self.output_dir, f"slide{slide_number}", "media"
        )
        os.makedirs(media_output_directory, exist_ok=True)
        
        # Generate background image file path
        background_filename = f"background_{slide_number}.png"
        background_path = os.path.join(media_output_directory, background_filename)
        
        # Get theme colors from html_writer's theme resolver
        theme_colors = None
        if self.html_writer.theme_resolver:
            # Build theme colors dictionary for background generation
            theme_colors = {
                "bg1": self.html_writer.theme_resolver.resolve_scheme_color("bg1"),
                "bg2": self.html_writer.theme_resolver.resolve_scheme_color("bg2"),
                "accent1": self.html_writer.theme_resolver.resolve_scheme_color("accent1"),
                "accent2": self.html_writer.theme_resolver.resolve_scheme_color("accent2"),
                "accent3": self.html_writer.theme_resolver.resolve_scheme_color("accent3"),
                "accent4": self.html_writer.theme_resolver.resolve_scheme_color("accent4"),
                "accent5": self.html_writer.theme_resolver.resolve_scheme_color("accent5"),
                "accent6": self.html_writer.theme_resolver.resolve_scheme_color("accent6"),
                "lt1": self.html_writer.theme_resolver.resolve_scheme_color("lt1"),
                "lt2": self.html_writer.theme_resolver.resolve_scheme_color("lt2"),
                "dk1": self.html_writer.theme_resolver.resolve_scheme_color("dk1"),
                "dk2": self.html_writer.theme_resolver.resolve_scheme_color("dk2"),
            }
            # Filter out None values
            theme_colors = {k: v for k, v in theme_colors.items() if v is not None}

        # Generate background image using the renderer with theme colors
        generated_path = self.background_renderer.generate_background_image(
            slide.common_slide_data,
            background_path,
            theme_colors
        )
        
        
        # Return relative path for HTML usage
        if generated_path:
            return f"media/{background_filename}"
        
        return None

    def parse_presentation(self):
        # Parse all presentation-level data using the new unified approach
        presentation = self.presentation_parser.parse()
        
        # Get the overall slide width and height from the presentation properties
        slide_width, slide_height = self.presentation_parser.get_slide_size()
        # Initialize the BackgroundRenderer with proper slide dimensions
        self.background_renderer = BackgroundRenderer(slide_width=1280, slide_height=720)
        # Get a list of all slide XML paths and their corresponding relationship file paths
        slide_paths = self._get_slide_paths_and_rels()

        slides = []
        # Iterate through each slide, processing them one by one
        for i, (slide_xml_file_path, slide_relationships_file_path) in enumerate(
            slide_paths
        ):
            # Calculate the 1-based slide number
            current_slide_number = i + 1
            
            # Process the current slide: parse its content, copy media, and write HTML/JSON output
            current_slide_parser = SlideParser(
                slide_xml_file_path,
                slide_relationships_file_path,
                self.pptx_unpacked_path,
                slide_width,
                slide_height,
                presentation=presentation,
            )
            # Parse the slide to get its structured data
            parsed_slide_data = current_slide_parser.parse_slide(
                slide_number=current_slide_number
            )
            slides.append(parsed_slide_data)

            # Generate background image for this slide
            background_image_path = self._generate_background_for_slide(
                parsed_slide_data, current_slide_number
            )
            
            # Set the generated background path on the slide object
            if background_image_path:
                parsed_slide_data.generated_background_path = background_image_path

            # Copy any media files associated with this slide to its output directory
            self._copy_media_for_slide(parsed_slide_data, current_slide_number)

            # Write the parsed slide data to HTML format
            self.html_writer.write_slide_html(parsed_slide_data, current_slide_number)

        # Create the JSON presentation
        json_presentation = self.json_writer.transform_to_json_presentation(
            slides, "galaxy-001", "Galaxy Presentation"
        )
        self.json_writer.write_presentation_json(json_presentation)

        print(f"Successfully parsed {len(slide_paths)} slides.")

"""Test Galaxy theme integration to debug background resolution."""

import os

from learnx_parser.writers.theme_resolver import ThemeResolver


def test_galaxy_theme_resolution():
    """Test theme resolution with actual Galaxy presentation files."""

    # Use the actual Galaxy presentation files
    pptx_path = "./temp_pptx"
    if not os.path.exists(pptx_path):
        print("Galaxy presentation files not found - skipping test")
        return

    # Initialize theme resolver
    resolver = ThemeResolver(pptx_path)

    # Load slide master color map
    slide_master_path = os.path.join(
        pptx_path, "ppt", "slideMasters", "slideMaster11.xml"
    )
    if os.path.exists(slide_master_path):
        resolver.load_slide_master_color_map(slide_master_path)

    # Debug output
    print(f"Theme name: {resolver.color_scheme.name}")
    print("Color scheme colors:")
    for color_name in ["dk1", "lt1", "dk2", "lt2", "accent1", "accent2"]:
        color_value = resolver.color_scheme.get_color(color_name)
        print(f"  {color_name}: #{color_value}")

    print("\nColor map:")
    for key, value in resolver.color_map.items():
        print(f"  {key} -> {value}")

    print(f"\nBackground fill styles: {len(resolver.background_fill_styles)}")
    for i, style in enumerate(resolver.background_fill_styles):
        print(f"  Style {i + 1} (idx={i + 1001}): {style.fill_type}")
        if style.color_ref:
            print(f"    Color ref: {style.color_ref}")
        else:
            print(f"    Direct color: #{style.color}")
        resolved_color = style.resolve_color(resolver.color_scheme)
        print(f"    Resolved color: #{resolved_color}")

    # Test background reference resolution (what slide master uses)
    print("\nBackground reference resolution:")
    bg_color = resolver.resolve_background_reference(1001, "bg1")
    print(f"  bgRef idx=1001 with schemeClr=bg1: #{bg_color}")

    # Test CSS generation
    css = resolver.get_background_css(1001, "bg1")
    print(f"  Generated CSS: {css}")

    # Test direct scheme color resolution
    print("\nDirect scheme color resolution:")
    bg1_color = resolver.resolve_scheme_color("bg1")
    print(f"  bg1 resolves to: #{bg1_color}")

    lt1_color = resolver.resolve_scheme_color("lt1")
    print(f"  lt1 resolves to: #{lt1_color}")

    dk1_color = resolver.resolve_scheme_color("dk1")
    print(f"  dk1 resolves to: #{dk1_color}")


if __name__ == "__main__":
    test_galaxy_theme_resolution()

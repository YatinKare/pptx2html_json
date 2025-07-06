"""
Common XML parsing utilities for the presentation parser.
"""

from lxml import etree


def parse_rels_file(rels_path):
    """
    Parse a relationships (.rels) file and return a dictionary of relationship IDs to targets.

    Args:
        rels_path (str): Path to the .rels file

    Returns:
        dict: Dictionary mapping relationship IDs to their target paths
    """
    relationships = {}
    try:
        relationships_tree = etree.parse(rels_path)
        for relationship in relationships_tree.findall(".//{*}Relationship"):
            relationships[relationship.get("Id")] = relationship.get("Target")
    except Exception as e:
        print(f"Warning: Could not parse relationships file {rels_path}: {e}")
    return relationships


def find_element_text(element, xpath, nsmap=None):
    """
    Find an element using XPath and return its text content.

    Args:
        element: The XML element to search within
        xpath (str): XPath expression to find the element
        nsmap (dict): Namespace map for the XPath expression

    Returns:
        str or None: The text content of the found element, or None if not found
    """
    found_element = element.find(xpath, namespaces=nsmap)
    return found_element.text if found_element is not None else None


def find_element_attribute(element, xpath, attribute, nsmap=None):
    """
    Find an element using XPath and return the value of a specific attribute.

    Args:
        element: The XML element to search within
        xpath (str): XPath expression to find the element
        attribute (str): Name of the attribute to retrieve
        nsmap (dict): Namespace map for the XPath expression

    Returns:
        str or None: The attribute value, or None if element or attribute not found
    """
    found_element = element.find(xpath, namespaces=nsmap)
    return found_element.get(attribute) if found_element is not None else None


def safe_int_attribute(element, attribute, default=0):
    """
    Safely convert an element attribute to an integer.

    Args:
        element: The XML element
        attribute (str): Name of the attribute
        default (int): Default value if attribute is missing or invalid

    Returns:
        int: The integer value of the attribute or the default value
    """
    try:
        value = element.get(attribute)
        return int(value) if value is not None else default
    except (ValueError, TypeError):
        return default


def safe_bool_attribute(element, attribute, default=False):
    """
    Safely convert an element attribute to a boolean.

    Args:
        element: The XML element
        attribute (str): Name of the attribute
        default (bool): Default value if attribute is missing

    Returns:
        bool: True if attribute value is "1" or "true", False otherwise
    """
    value = element.get(attribute)
    if value is None:
        return default
    return value.lower() in ("1", "true")

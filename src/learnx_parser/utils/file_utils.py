"""
File utility functions for finding and managing presentation files.
"""

import glob
import os


def find_files(directory, pattern):
    """
    Find all files matching a pattern recursively within a directory.
    
    Args:
        directory (str): The directory to search in
        pattern (str): The file pattern to match (e.g., "slideMaster*.xml")
        
    Returns:
        list[str]: List of file paths matching the pattern
    """
    if not os.path.exists(directory):
        return []
    
    # Use ** for recursive searching
    search_pattern = os.path.join(directory, "**", pattern)
    return glob.glob(search_pattern, recursive=True)
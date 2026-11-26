# ===========================================
# WRITER FILE - Save and Load Data
# ===========================================
# 
# This file handles reading and writing files
# We can only use os (or pathlib) and csv as allowed

import os
import csv


def get_save_path():
    """
    Find and create the saves folder
    Returns the path to the saves folder
    """
    # Get where this file is located
    current_file_location = os.path.abspath(__file__)
    # Get the folder containing this file
    current_folder = os.path.dirname(current_file_location)
    # Create path to saves folder
    save_folder = os.path.join(current_folder, "saves")
    
    # Create saves folder if it doesn't exist
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    
    return save_folder


def sanitize_save_name(name):
    """
    Clean up a save name to make it safe for filenames
    Removes spaces, special characters etc.
    
    Returns cleaned name, or None if invalid
    """
    if name is None:
        return None
    
    # Convert to string
    name_string = str(name)
    # Remove leading/trailing spaces
    name_string = name_string.strip()
    # Replace spaces with underscores
    name_string = name_string.replace(" ", "_")
    
    # Check for empty
    if name_string == "":
        return None
    # Check for dots only
    if name_string == "." or name_string == "..":
        return None
    # Check for slashes (path separators)
    if "/" in name_string or "\\" in name_string:
        return None
    if os.sep in name_string:
        return None
    
    return name_string


def create_save(save_name):
    """
    Create a new empty save file
    Returns True if successful, False if failed
    """
    clean_name = sanitize_save_name(save_name)
    if clean_name is None:
        return False
    
    save_folder = get_save_path()
    file_path = os.path.join(save_folder, clean_name)
    
    try:
        # Don't overwrite if exists
        if os.path.exists(file_path):
            return False
        # Create empty file
        with open(file_path, "x"):
            pass  # Do nothing
        # Create the file do nothing and close the file and return that the file has been created(true)
        return True
    except OSError:
        return False


def write_file(file_name, data):
    """
    Write data to a file using CSV format
    data should be a list of lists
    Returns True if successful
    """
    clean_name = sanitize_save_name(file_name)
    if clean_name is None:
        return False
    
    save_folder = get_save_path()
    file_path = os.path.join(save_folder, clean_name)
    
    try:
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)
        return True
    except OSError:
        return False


def read_file(file_name):
    """
    Read data from a CSV file
    Returns list of lists, or None if failed
    """
    clean_name = sanitize_save_name(file_name)
    if clean_name is None:
        return None
    
    save_folder = get_save_path()
    file_path = os.path.join(save_folder, clean_name)
    
    if not os.path.isfile(file_path):
        return None
    
    try:
        rows = []
        with open(file_path, "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(row)
        return rows
    except OSError:
        return None

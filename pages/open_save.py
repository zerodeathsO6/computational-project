# OPEN SAVE PAGE
# This page lets the user open an existing save

from utils import check_if_exist, generate_question
from writer import read_file, sanitize_save_name
from pages.save_menu import save_menu


def open_save(state):
    # Only run if we're on open save page (state[0] == 1)
    if state[0] == 1:
        # Ask user which save to open
        raw_name = generate_question("Which save to open? (blank to cancel)", "str")
        raw_name = raw_name.strip()
        
        # Start by going back to menu
        state = [0, ""]
        
        # If they entered nothing, cancel
        if raw_name == "":
            return state
        
        # Clean the name
        clean_name = sanitize_save_name(raw_name)
        
        if clean_name is None:
            print("= That save name is not valid =")
            return state
        
        # Check if the save exists
        if not check_if_exist(clean_name):
            print("Please enter a valid save.")
            return state
        
        # Try to read the save file
        rows = read_file(clean_name)
        
        if rows is None:
            print("= Could not read that save =")
            return state
        
        # Go to save menu with the data
        save_menu(rows)
        
        # Return to main menu
        return state
    
    return state

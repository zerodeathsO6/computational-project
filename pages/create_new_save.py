# CREATE NEW SAVE PAGE
# This page lets the user create a new save file

from utils import generate_question
from writer import create_save, sanitize_save_name


def create_new_save(state):
    # Only run if we're on create new save page (state[0] == 2)
    if state[0] == 2:
        # Ask user for save name
        raw_name = generate_question("Please enter a save name (blank to cancel)", "str")
        
        # Clean the name
        clean_name = sanitize_save_name(raw_name)
        
        if clean_name is None:
            # Check if they just pressed enter (cancel)
            if raw_name.strip():
                # They tried to enter an invalid name
                print("= That save name is not valid =")
            # If blank, just cancel and go back to menu
        else:
            # Try to create the save
            success = create_save(clean_name)
            if success:
                print("= Save has been created succesfully =")
            else:
                print("= A save with that name already exists =")
        
        # Go back to main menu
        state = [0, ""]
    
    return state

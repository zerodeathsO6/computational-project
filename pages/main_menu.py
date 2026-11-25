# MAIN MENU PAGE
# This shows the main menu with options: Open save, Create new save, List saves, Exit

from utils import generate_questionnaire


def main_menu(state):
    # Only run if we're on the main menu (state[0] == 0)
    if state[0] == 0:
        # List of menu options
        options = ["Open save", "Create new save", "List saves", "Exit"]
        
        # Ask user to choose
        answer = generate_questionnaire("Choose an option", options)
        
        # Based on the answer, go to the right page
        if answer == 0:
            # Go to open save page
            state = [1, ""]
        elif answer == 1:
            # Go to create new save page
            state = [2, ""]
        elif answer == 2:
            # Go to list saves page
            state = [3, ""]
        elif answer == 3:
            # Exit the program (state 4 means exit)
            state = [4, ""]
        else:
            # If something unexpected, stay on main menu
            state = [0, ""]
    
    return state

# ===========================================
# MAIN ENTRY POINT FOR THE FIXTUREFORGE APP (VERSION 2)
# ===========================================
# 
# This is the starting file of our program.
# Think of this like the "brain" that connects different parts together.
# 
# What it does:
# 1. Shows the app header (title)
# 2. Keeps track of which menu/page we're on using a state variable
# 3. Switches between different pages based on user choices
# 4. Runs in a loop until the user chooses to exit

# Import helper functions for formatting (making things look nice)
from format import app_header

# Import the different menu pages we need
# Each page is a different screen the user sees
from pages.main_menu import main_menu
from pages.create_new_save import create_new_save
from pages.list_saves import list_saves
from pages.open_save import open_save


def main():
    """
    This is the main function - it runs when the program starts.
    
    state is a list that keeps track of where we are in the program:
    - state[0] = current screen/page number
      * 0 = Main Menu
      * 1 = Open an existing save
      * 2 = Create a new save
      * 3 = List all saves
      * 4 or more = Exit the program
    - state[1] = extra information we might need to pass between pages (not used much here)
    """
    # Create the state list to track which page we're on
    state = [0, ""]

    # Show the app header at the beginning
    app_header()

    try:
        # Keep running the program until we get an exit signal
        # This is an infinite loop - it only breaks when we choose to exit
        while True:
            # Get the current page number
            current_page = state[0]

            # Check which screen/page we should show based on current_page
            if current_page == 0:
                # Page 0 = Main Menu (where you choose what to do)
                state = main_menu(state)

            elif current_page == 1:
                # Page 1 = Open an existing save file
                state = open_save(state)

            elif current_page == 2:
                # Page 2 = Create a new save file
                state = create_new_save(state)

            elif current_page == 3:
                # Page 3 = List all save files
                state = list_saves(state)

            else:
                # Any other number (like 4) means we want to exit the program
                break

    except EOFError:
        # If the user closes input (like pressing Ctrl+D), exit nicely without errors
        print()
    except KeyboardInterrupt:
        # If the user presses Ctrl+C, exit nicely without showing an error
        print()

    # Say goodbye when the program ends
    print("Goodbye!")


# This special line runs the main function when we start the program
# (It won't run if we import this file from somewhere else)
if __name__ == "__main__":
    main()
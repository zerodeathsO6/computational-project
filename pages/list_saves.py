# LIST SAVES PAGE
# This page shows all the save files that exist

from utils import list_save
from format import gen_space


def list_saves(state):
    # Only run if we're on list saves page (state[0] == 3)
    if state[0] == 3:
        gen_space()
        
        # Get all save files
        saves = list_save()
        
        if len(saves) == 0:
            # No saves exist yet
            print("(no saves yet)")
        else:
            # Show each save file
            for save_name in saves:
                print(f"= {save_name} =")
        
        # Go back to main menu
        state = [0, ""]
    
    return state

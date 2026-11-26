# ===========================================
# UTILS FILE - Helper functions for user input
# ===========================================
# 
# This file has simple helper functions to talk to the user.
# When you ask a user for input, you need to check if it's valid.
# These functions do that for you in a simple way.

import os
from format import gen_space
from writer import get_save_path, sanitize_save_name


def check_if_exist(save_name):
    """
    Check if a save file with this name exists
     
    Args:
        save_name: The name of the save file to check
         
    Returns:
        True if the file exists, False if it doesn't
    """
    # Clean up the name first (remove spaces, etc.)
    clean_name = sanitize_save_name(save_name)
    
    # If the name is not valid, the file can't exist
    if clean_name is None:
        return False
    
    # Find the save folder
    save_folder = get_save_path()
    
    # Build the full path to the file
    file_path = os.path.join(save_folder, clean_name)
    
    # Check if the file exists and is a normal file
    if os.path.isfile(file_path):
        return True
    else:
        return False


def generate_question(question, answer_type, outputs=None):
    """
    Ask the user a question and get their answer
    
    Args:
        question: The question to ask (as text)
        answer_type: Can be "int" (for numbers) or "str" (for text)
        outputs: Optional - a list of allowed answers. If provided, only these are accepted.
        
    Returns:
        The user's answer - as an int if answer_type is "int", or as a string if "str"
    """
    # Keep asking until we get a valid answer
    while True:
        if answer_type == "int":
            # Asking for a number
            try:
                # Show the question to the user
                print(f"= {question} =")
                # Get input from user
                user_input = input("")
                # Try to convert the input to an integer (whole number)
                answer = int(user_input)
                
                # Check if we need to restrict to certain answers
                if outputs is None:
                    # Any number is fine
                    return answer
                else:
                    # Only certain numbers are allowed
                    if answer in outputs:
                        return answer
                    else:
                        # The number is not in the allowed list
                        gen_space()
                        print("Please enter an answer that is a valid choice")
                        # Go back to ask again
                        continue
            
            except ValueError:
                # If the user didn't enter a number (like typing "abc")
                gen_space()
                print("Please enter a number as your answer")
                # Go back to ask again
                continue
        
        elif answer_type == "str":
            # Asking for text
            # Show the question
            print(f"= {question} =")
            # Get input from user
            user_input = input("")
            
            # Check if we need to restrict to certain answers
            if outputs is None:
                # Any text is fine
                return user_input
            else:
                # Only certain answers are allowed
                if user_input in outputs:
                    return user_input
                else:
                    # Not in the allowed list
                    gen_space()
                    print("Please enter an answer that is a valid choice")
                    # Go back to ask again
                    continue
        
        else:
            # If someone passes wrong answer_type, raise an error
            raise ValueError(f"Unknown answer type: {answer_type!r}")


def generate_questionnaire(heading, options):
    """
    Show a menu with numbered options and ask user to choose one
    
    Args:
        heading: The title of the menu
        options: A list of option names (each is a string)
        
    Returns:
        The index of the chosen option (starting from 0)
    """
    gen_space()
    
    # Show the heading
    print(f"= {heading} =")
    
    # Show each option with a number next to it
    i = 0
    while i < len(options):
        option_number = i + 1  # Start counting from 1 for users
        option_text = options[i]
        print(f"{option_number}: {option_text}")
        i = i + 1
    
    gen_space()
    
    # Ask user to pick an option
    while True:
        try:
            # Show the prompt
            prompt = f"Please choose your desired option (1-{len(options)}): "
            user_input = input(prompt)
            # Convert to number
            choice = int(user_input)
            
            # Check if the choice is valid (between 1 and number of options)
            if choice >= 1 and choice <= len(options):
                # Return zero-based index (easier to use in code)
                return choice - 1
            else:
                # Choice is out of range
                gen_space()
                print(f"Please choose a number between 1 and {len(options)}")
                # Ask again
        
        except ValueError:
            # User didn't enter a number
            gen_space()
            print(f"Please choose a number between 1 and {len(options)}")
            # Ask again


def list_save():
    """
    Get a list of all save files in the saves folder
    
    Returns:
        A list of save filenames, sorted alphabetically
    """
    # Get the saves folder
    save_folder = get_save_path()
    
    try:
        # Get all files in the saves folder
        files = os.listdir(save_folder)
        # Sort them alphabetically
        files.sort()
        return files
    
    except OSError:
        # If something goes wrong, return empty list
        return []

# Code Explanation for Version 2

This document explains every file in simple terms

## 1. mn.py (Main File)
The entry point. It uses a state machine, keeps track of current page. 
States: 0=main menu, 1=open save, 2=create save, 3=list saves, else=exit.
Uses a while loop to stay running until exit.

## 2. format.py
Just two simple functions to print lines, keeps things consistent so that there isn't too much of a discrepancy in how each page looks.
- app_header(): prints the title
- gen_space(): prints blank line

## 3. writer.py
Handles all file operations using only os and csv.
- get_save_path(): finds/creates saves folder
- sanitize_save_name(): makes names safe for files
- create_save(): creates empty file
- write_file(): saves data as CSV
- read_file(): reads CSV data

## 4. utils.py
Helper functions for user interaction.
- check_if_exist(): checks if save exists
- generate_question(): asks question, validates input
- generate_questionnaire(): shows menu, gets choice
- list_save(): lists all saves

## 5. tournament.py
Implements Round Robin scheduling and tables.
- generate_round_robin_teams(): creates team names
- generate_round_robin_fixtures(): creates all pairings
- calculate_standings(): computes table from results
- format_table_row(): formats rows for display

## 6. pages/main_menu.py
Shows 4 options: Open, Create, List, Exit. Returns new state.

## 7. pages/create_new_save.py
Asks for name, creates file if valid and unique.

## 8. pages/list_saves.py
Shows all saves or "(no saves yet)".

## 9. pages/open_save.py
Opens a save and goes to save menu.

## 10. pages/save_menu.py
Interactive tournament manager with full Round Robin system and tabular display.

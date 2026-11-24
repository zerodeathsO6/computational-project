# ===========================================
# TOURNAMENT HELPER FUNCTIONS
# ===========================================
# 
# This file contains functions for Round Robin tournaments
# ROUND ROBIN = Every team plays every other team once
# 
# Simple Python - easy to understand line by line

def generate_round_robin_teams(num_teams):
    """
    Create a list of team names
    If we don't know team names, we create default ones like Team 1, Team 2 etc.
    
    Args:
        num_teams: How many teams there are (as a number)
    
    Returns:
        A list containing team names
    """
    teams = []
    i = 1
    # Loop from 1 to num_teams
    while i <= num_teams:
        # Create team name
        team_name = "Team " + str(i)
        # Add to list
        teams.append(team_name)
        i = i + 1  # Go to next team
    
    return teams


def generate_round_robin_fixtures(teams):
    """
    Generate all matches for a round robin tournament
    In a single round robin, each team plays every other team once
    
    Args:
        teams: A list of team names
        
    Returns:
        A list of fixtures. Each fixture is [match_id, team1, team2, result]
        result starts empty as ""
    """
    fixtures = []
    match_id = 1
    num_teams = len(teams)
    
    # Generate all pairings where first team comes before second
    i = 0
    while i < num_teams:
        j = i + 1
        while j < num_teams:
            team1 = teams[i]
            team2 = teams[j]
            # Create a fixture: [match_id, team1, team2, result]
            fixture = [str(match_id), team1, team2, ""]
            fixtures.append(fixture)
            match_id = match_id + 1  # Increase match number
            j = j + 1  # Next opponent
        i = i + 1  # Next team
    
    return fixtures


def calculate_standings(teams, fixtures):
    """
    Calculate league table standings from results
    
    Points system (simple):
    - Win = 3 points
    - Draw = 1 point
    - Loss = 0 points
    
    Args:
        teams: List of team names
        fixtures: List of fixtures with results
        
    Returns:
        Sorted list of teams with stats
        Each: [team, played, won, drawn, lost, points, gf, ga, gd]
        Pld = Played, W=Won, D=Drawn, L=Lost, Pts=Points
        GF=Goals For, GA=Goals Against, GD=Goal Difference
    """
    standings = []
    
    # Initialize standings for each team
    for team in teams:
        # [team_name, played, won, drawn, lost, points, goals_for, goals_against, goal_diff]
        team_stats = [team, 0, 0, 0, 0, 0, 0, 0, 0]
        standings.append(team_stats)
    
    # Process each fixture
    for fixture in fixtures:
        team1 = fixture[1]
        team2 = fixture[2]
        result = fixture[3]
        
        # Skip if not played yet
        if result == "":
            continue
        
        # Parse result like "3-2" (team1 got 3, team2 got 2)
        if "-" in result:
            try:
                # Split by dash
                parts = result.split("-")
                goals1_str = parts[0].strip()
                goals2_str = parts[1].strip()
                goals1 = int(goals1_str)
                goals2 = int(goals2_str)
                
                # Find teams in standings
                team1_index = -1
                team2_index = -1
                k = 0
                while k < len(standings):
                    if standings[k][0] == team1:
                        team1_index = k
                    if standings[k][0] == team2:
                        team2_index = k
                    k = k + 1
                
                if team1_index == -1 or team2_index == -1:
                    continue  # Team not found
                
                # Update played games
                standings[team1_index][1] = standings[team1_index][1] + 1
                standings[team2_index][1] = standings[team2_index][1] + 1
                
                # Update goals for/against
                standings[team1_index][6] = standings[team1_index][6] + goals1  # GF
                standings[team1_index][7] = standings[team1_index][7] + goals2  # GA
                standings[team2_index][6] = standings[team2_index][6] + goals2  # GF
                standings[team2_index][7] = standings[team2_index][7] + goals1  # GA
                
                # Calculate goal difference
                standings[team1_index][8] = standings[team1_index][6] - standings[team1_index][7]
                standings[team2_index][8] = standings[team2_index][6] - standings[team2_index][7]
                
                # Decide win/draw/loss and points
                if goals1 > goals2:
                    # Team 1 won
                    standings[team1_index][2] = standings[team1_index][2] + 1  # Won
                    standings[team1_index][5] = standings[team1_index][5] + 3  # Points
                    standings[team2_index][4] = standings[team2_index][4] + 1  # Lost
                elif goals2 > goals1:
                    # Team 2 won
                    standings[team2_index][2] = standings[team2_index][2] + 1  # Won
                    standings[team2_index][5] = standings[team2_index][5] + 3  # Points
                    standings[team1_index][4] = standings[team1_index][4] + 1  # Lost
                else:
                    # Draw
                    standings[team1_index][3] = standings[team1_index][3] + 1  # Drawn
                    standings[team1_index][5] = standings[team1_index][5] + 1  # Points
                    standings[team2_index][3] = standings[team2_index][3] + 1  # Drawn
                    standings[team2_index][5] = standings[team2_index][5] + 1  # Points
                
            except ValueError:
                # Skip invalid result format
                pass
            except IndexError:
                # Skip if format is wrong
                pass
    
    # sort standings by points first (high to low), then goal difference (high to low)
    sorted_standings = sorted(standings, key=lambda x: (x[5], x[8]), reverse=True)
    
    return sorted_standings


def format_table_row(cols, widths):
    """
    Format a single row to look nice in a table
    
    Args:
        cols: List of values for each column
        widths: How wide each column should be
        
    Returns:
        A nicely formatted string
    """
    parts = []
    i = 0
    while i < len(cols):
        col_str = str(cols[i])
        width = widths[i]
        # Make sure it's not too long or too short
        if len(col_str) < width:
            # Add spaces to pad
            padding = " " * (width - len(col_str))
            col_str_padded = col_str + padding
        elif len(col_str) > width:
            # Cut it short if too long
            col_str_padded = col_str[:width]
        else:
            col_str_padded = col_str
        parts.append(col_str_padded)
        i = i + 1
    
    # Join with | to make colmns
    return " | ".join(parts)
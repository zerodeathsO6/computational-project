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
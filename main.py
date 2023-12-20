# Using tabulate to visualize the table
from tabulate import tabulate
import json

# Load the JSON file to handle
with open('teams.json', 'r') as f:
    win_loss_data = json.load(f)

# Base table to add to, headers will be team names
table = []
headers = ["Tm"]

# Iterate through the dict
for team, team_data in win_loss_data.items():
    # Add new team to headers, each row begins with the new team
    headers.append(team)
    row = [team]

    # Used to signify need for dashes
    counter = 0

    # Iterate through the head-to-head data for the team
    for sub_team, win_data in team_data.items():
        # If the table has rows equal to the counter, the teams are the same
        if counter == len(table):
            row.append("--")
        
        # Need to append win data even if dashes are added, this correctly aligns the table
        row.append(win_data["W"])
        counter += 1

    # Needed for the final space in the table
    if "--" not in row:
        row.append("--")
    
    # Adds to 2D list that makes the table
    table.append(row)

# Simulate the footer of the table
table.append(headers)

# Table display
print(tabulate(table, headers, tablefmt="plain"))
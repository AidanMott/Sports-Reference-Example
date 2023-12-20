# Using this to visualize the table
from tabulate import tabulate

import json

with open('teams.json', 'r') as f:
    win_loss_data = json.load(f)

table = []
headers = ["Tm"]

for team, team_data in win_loss_data.items():
    headers.append(team)
    row = [team]
    counter = 0
    for sub_team, win_data in team_data.items():
        if counter == len(table):
            row.append("--")
        row.append(win_data["W"])
        counter += 1
    if "--" not in row:
        row.append("--")
    table.append(row)

print(tabulate(table, headers, tablefmt="plain"))
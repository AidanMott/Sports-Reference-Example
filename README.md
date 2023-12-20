# Sports-Reference-Example

main.py contains the code example I am providing. 
My process was to create a nested list in Python using data from the JSON file.
After the code imports the data from the JSON file and creates empty lists to represent the tables, it iterates through the data and builds the list with each loop.

In each loop, the code will:
 * add the current team to the table heading and first column,
 * iterate through the win-loss data for the current team,
 * use a counter to determine whether the table space needs dashes or not,
 * and add the win data from the corresponding team.

The final output is then formatted using the tabulate library.

It is important to note that this code largely assumes that the JSON file given preserves the alphabetical order of the teams.
If this were not the case, I would have to edit the code so that the loop searches for each team instead of using the simple structure of the code I wrote.

One way this could be approached is by first laying out the labels for both the rows and the columns so that the table has every team listed.
After this is done, the code would then fill in each space by searching the data structure for each corresponding value, while adding dashes if the row and column are the same team.
This method is not quite as simple as the one I wrote, but would be my approach given potentially "messier" JSON files.

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

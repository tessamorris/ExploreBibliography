# Packages to Import 
import pandas as pd # install pandas
import os.path
from os import path

# Checks if a data file exists. If it doesn't exist it will create it 
def checkFileExistence(file):
    output_exists = os.path.exists(file)
    if not output_exists:
        print(file + " does not exist.")
    return output_exists

# Ask for a numerical input 
def askIntegerInput(inputstr,maxval):
    # Initialize a boolean statemennt 
    enteredinput = False
    while not enteredinput:
        # Ask the user the question 
        int_input = input(inputstr + ": ")
        # Create a boolean statement to check if the input was a number or not 
        is_integer = True 
        # Check if the current input is a number or not 
        try:
           val = int(int_input)
        except ValueError:
            is_integer = False

        if is_integer:
            ansval = int(int_input)
            if ansval >= 0 and ansval <= maxval:
                return ansval 
                enteredinput = True 

# Check the existance of a literature notes file summary
bibnotesfile = "bibnotes.csv"
bibnotes_exist = checkFileExistence(bibnotesfile)
if bibnotes_exist:
    bibnotes_df = pd.read_csv(bibnotesfile)
    # Remove the first column, which is old indices 
    bibnotes_df = bibnotes_df[bibnotes_df.columns[1:]]
    # Remove the old indexes
    bibnotes_df = bibnotes_df.reset_index(drop=True)
    # Ask the user how they would like to explore their data 
    d = {'Exploration Type': ['See All', 'See Category']}
    howexplore_df = pd.DataFrame(data=d)
    print(howexplore_df)
    ansval = askIntegerInput("Enter how you would like to explore your data (Enter the number)", len(howexplore_df))
    print(howexplore_df['Exploration Type'].iloc[ansval])
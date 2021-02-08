# Packages to Import 
import pandas as pd # install pandas
import os.path
from os import path
from datetime import datetime, timedelta

# Define a python function that displays the current date 
def getTimeDay(str):
    # Get the current date and time 
    current_datetime = datetime.now() # current date and time

    # Store the current day and time 
    current_date = current_datetime.strftime("%Y-%m-%d")
    current_time = current_datetime.strftime("%H:%M:%S")
    # Print the current date and time 
    print ("Today's date: " + current_date) 
    print ( str + " time: " + current_time)

    # Output the current date and time 
    return current_datetime, current_date, current_time

# Checks if a data file exists. If it doesn't exist it will create it 
def checkFileExistence(file):
    output_exists = os.path.exists(file)
    if not output_exists:
        print(file + " does not exist.")
    return output_exists

# Check the existance of a literature notes file summary
bibnotesfile = "bibnotes.csv"
bibnotes_exist = checkFileExistence(bibnotesfile)

# Check the existance of a literature notes file summary
reffile = "refs.csv"
refs_exist = checkFileExistence(reffile)
if refs_exist:
    refs_df = pd.read_csv(reffile)

enteredinput = False
while not enteredinput:
    # Ask if the user would like to enter a CSV file or add the entry manually
    howadd_input = input("Would you like to [0] Add a CSV file or [1] Add an entry manually?: ")

    # Create a boolean statement to check if the input was a number or not 
    is_integer = True 
    # Check if the current mood is a number or not 
    try:
       val = int(howadd_input)
    except ValueError:
        is_integer = False

    if is_integer:
        howadd = int(howadd_input)
        if howadd == 0 or howadd == 1:
            enteredinput = True 

# CSV option first
if howadd == 0:
    # Load the file 
    newentry_exist = False
    while not newentry_exist:
        newentryfile = input("What is the name of your new entry CSV file (include .csv): ")
        newentry_exist = checkFileExistence(newentryfile)
    # Load the new entry file
    newentry_df = pd.read_csv(newentryfile)
    # Get the number of new entries 
    numentry = len(newentry_df.index)
    for biben in newentry_df['BibTexKey']:
        print(biben)
        cross_df = refs_df[refs_df['BibTexKey'] == biben]
        print(cross_df)


# # Create the new mood in a dataframe 
# mood_dfnew = pd.DataFrame({'Moods': [current_mood]})    
# # Append the data frame with the new data
# mood_df = mood_df.append(mood_dfnew, ignore_index=True)
# # Sort the moods alphabetically 
# mood_df = mood_df.sort_values(by=['Moods'])
# # Remove the old indexes
# mood_df = mood_df.reset_index(drop=True)
# # Export the csv file 
# mood_df.to_csv(r'moods.csv')  
# Add many paper to categories 
# Add notes to paper 
# Browse through cateogires
# Make references .bib file its own function 

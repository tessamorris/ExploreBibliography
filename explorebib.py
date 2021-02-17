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
def askDfInput(inputstr,inputdf,colname):
    # Display the dataframe
    print(inputdf)
    # Set the max value to the length of the dataframe 
    maxval = len(inputdf)
    # Initialize a boolean statemennt 
    enteredinput = False
    while not enteredinput:
        # Ask the user the question 
        ans_input = input(inputstr + ": ")
        # Check if the answer occurs in the dataframe 
        ans_df = inputdf[inputdf[colname] == ans_input]
        # Initialize boolean statement to check for an integer answer
        checkInt = False 
        if ans_df.empty: 
            # If the answer does not occur in the dataframe check if it is an integer value 
            checkInt = True 
        else: 
            # Get the number of answers 
            num_ans = len(ans_df)
            # If there is only one match then return the answer  
            if num_ans == 1: 
                finalans_intermediate = ans_df.tolist()
                finalans = finalans_intermediate[0]
                return finalans
                enteredinput = True 
            else:
                checkInt = True 

        if checkInt: 
            # Create a boolean statement to check if the input was a number or not 
            is_integer = True 
            # Check if the current input is a number or not 
            try:
               val = int(ans_input)
            except ValueError:
                is_integer = False
            # If the entry is an integer of the correct size, output the results 
            if is_integer:
                ansval = int(ans_input)
                if ansval >= 0 and ansval <= maxval:
                    finalans = inputdf[colname].iloc[ansval]
                    return finalans 
                    enteredinput = True 


# Checks if a data file exists. If it doesn't exist it will create it 
def list2string(lst):
    if lst:
        fcnt = 0 
        for ni in lst:
            if str(ni) != 'nan':
                if fcnt == 0: 
                    lststr = ni
                else: 
                    lststr = lststr + " " + ni
                fcnt = fcnt + 1 
    else:
        lststr = 'nan'
    return lststr

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
    howexplore_col = 'Exploration Type'
    howexplore_opts = ['All', 'Category', 'Keywords']
    d = {howexplore_col: howexplore_opts}
    howexplore_df = pd.DataFrame(data=d)
    howexplore_str = "Enter how you would like to explore your data? (Enter the number or string)"
    howexp = askDfInput(howexplore_str,howexplore_df,howexplore_col)

    # Spacing between entries 
    sepstr = "----------------------------------------------------------------"
    spcstr = '    '
    if howexp == 'All':
        # Sort alphabetically by bibtexkey
        bibnotes_df = bibnotes_df.sort_values(by=['BibTexKey'])
        # Get unique bibtexkeys, convert it to a list and then sort 
        ubibkeys = bibnotes_df['BibTexKey'].unique()
        for bi in ubibkeys:
            print(sepstr)
            currentbib_df = bibnotes_df[bibnotes_df['BibTexKey'] == bi]

            # Get the title 
            title_all = currentbib_df['Title'].unique().tolist()
            title_str = title_all[0]
            print( bi + ": " + title_str)

            # Get the categories 
            category_all = currentbib_df['Category'].unique().tolist()
            if category_all:
                catstr = spcstr + "Categories:"
                catstr_org = catstr
                for ci in category_all:
                    if str(ci) != 'nan':
                        catstr = catstr + " " + ci
                if catstr_org != catstr:
                    print(catstr)

            # Get the notes 
            notes_all = currentbib_df['Notes'].tolist()
            if notes_all:
                notestr = spcstr + "Notes:"
                notestr_org = notestr
                for ni in notes_all:
                    if str(ni) != 'nan':
                        catstr = catstr + " " + ci
                if catstr_org != catstr:
                    print(catstr)


            # Get the quotes 
        # Sort by bibtex key 
        # Display Title (bibtexkey)
        # Display Categories (only unique)
        # Display Notes (by date)
        # Display Quotes (by date)

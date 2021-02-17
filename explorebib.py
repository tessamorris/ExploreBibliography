# Packages to Import 
import pandas as pd # install pandas
from pandas import DataFrame
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
            print(spcstr)
            print(sepstr)
            print(spcstr)
            currentbib_df = bibnotes_df[bibnotes_df['BibTexKey'] == bi]

            # Get the title 
            title_all = currentbib_df['Title'].unique().tolist()
            title_str = title_all[0]
            print( bi + ": " + title_str)

            # Get the categories 
            category_all = currentbib_df['Category'].dropna().unique().tolist()
            catstr = list2string(category_all)
            if str(catstr) != 'nan':
                print("Categories: " + catstr)

            # Get the notes 
            notes_df = currentbib_df['Notes'].dropna()
            if not notes_df.empty:
                print("Notes:")
                for ni in notes_df:
                    print(spcstr + ni)

            # Get the quotes
            quote_df = currentbib_df['Quote'].dropna()
            if not quote_df.empty:
                print("Quotes:")
                for ni in quote_df:
                    print(spcstr + ni)
    elif howexp == 'Category':
        bibnotes_df = bibnotes_df.sort_values(by=['Category'])
        ucategories_all = bibnotes_df['Category'].dropna().unique().tolist()
        ucategories_df = DataFrame(ucategories_all, columns=['Category'])
        catsel = askDfInput('Select a category', ucategories_df, 'Category')
        bibnotes_catdf = bibnotes_df[bibnotes_df['Category'] == catsel]
        bibnotes_catdf = bibnotes_catdf.sort_values(by=['BibTexKey']).reset_index(drop=True)
        print(bibnotes_catdf['BibTexKey'])
        namesv = input('Enter the desired name of the csv file (include .csv): ')
        if namesv:
            bibnotes_catdf.to_csv(namesv)

    elif howexp == 'Keywords':
        print('Keywords to be implemented')
            # if notes_all:
            #     notestr = spcstr + "Notes:"
            #     notestr_org = notestr
            #     for ni in notes_all:
            #         if str(ni) != 'nan':
            #             catstr = catstr + " " + ci
            #     if catstr_org != catstr:
            #         print(catstr)


            # Get the quotes 
        # Sort by bibtex key 
        # Display Title (bibtexkey)
        # Display Categories (only unique)
        # Display Notes (by date)
        # Display Quotes (by date
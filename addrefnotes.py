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

# Check the existance of a literature notes file summary
bibnotesfile = "bibnotes.csv"
bibnotes_exist = checkFileExistence(bibnotesfile)

# Check the existance of a literature notes file summary
reffile = "refs.csv"
refs_exist = checkFileExistence(reffile)

# Add many paper to categories 
# Add notes to paper 
# Browse through cateogires
# Make references .bib file its own function 
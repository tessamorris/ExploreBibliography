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
if bibnotes_exist:
    bibnotes_df = pd.read_csv(bibnotesfile)
    # Remove the first column, which is old indices 
    bibnotes_df = bibnotes_df[bibnotes_df.columns[1:]]
    # Remove the old indexes
    bibnotes_df = bibnotes_df.reset_index(drop=True)
    print(bibnotes_df)
    # Find the duplicates
    cleanbibnotes_df = bibnotes_df.drop_duplicates()
    print(cleanbibnotes_df)
from pybtex.database.input import bibtex
import pandas as pd # install pandas

# Open the bibtex file 
parser = bibtex.Parser()
bibdata = parser.parse_file("references.bib")

# Generate a dataframe of all of the entries in the dataframe 
for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    try:
        # Store all of the useful information
        c_bibid = bib_id
        c_title = b["title"]
        c_year = b["year"]

        # Get the first author
        allauths = bibdata.entries[bib_id].persons["author"]
        c_auth1 = allauths[0]

        # Create the next entry
        ref_dfnew = pd.DataFrame({'BibTexKey': [c_bibid], 'Title': [c_title], 
            'Year': [c_year], 'FirstAuthor': [c_auth1]})

        # Check if the database has been created yet, if not, create it 
        rdbExists = "ref_df" in locals()

        if not rdbExists:
            ref_df = ref_dfnew
        else:
            ref_df = ref_df.append(ref_dfnew, ignore_index = True)
            ref_df = ref_df.sort_values(by='BibTexKey')
            ref_df = ref_df.reset_index(drop=True)


    # field may not exist for a reference
    except(KeyError):
        continue

# Save the references csv. 
ref_df.to_csv(r'refs.csv')
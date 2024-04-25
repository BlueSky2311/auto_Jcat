import pandas as pd
import os

# Specify the directory where the input file is stored
directory = "C:\\Users\\Blue\\Downloads\\test"

# Specify the name of the new subfolder
subfolder = "splited_sequences"

# Create the new subfolder if it doesn't exist
os.makedirs(os.path.join(directory, subfolder), exist_ok=True)

# Read the csv file
df = pd.read_csv(os.path.join(directory, 'JCat_test.csv')) #change the file name to the name of the file you want to split

# Loop through each row in the dataframe
for index, row in df.iterrows():
    # Open a new text file in the new subfolder with the Locus_tag as the name
    with open(os.path.join(directory, subfolder, f"{row['Locus_tag']}.txt"), 'w') as f:
        # Write the Sequence to the file
        f.write(row['Sequence'])
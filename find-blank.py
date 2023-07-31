import pandas as pd

# Read the CSV file into a pandas DataFrame
file_path = '/Users/femisokoya/Documents/GitHub/flytipping/Flytipping_updated.csv'
df = pd.read_csv(file_path)

# For every blank value in the 'ons code' column, print the corresponding value from the 'LA Name' column
for index, row in df.iterrows():
    if pd.isnull(row['ONS Code']):
        print(row['LA Name'])

import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('interim1.csv')

# Replace blank values and ":" with 0 in the "Total Incidents" column
# df['Total Incidents'] = df['Total Incidents'].fillna('0').replace(':', '0')

# Replace blank values and ":" with 0 in the "numerical" column and cast as float
df['numerical'] = df['numerical'].fillna('0').replace(':', '0').astype(float)

# Save the modified DataFrame to a new CSV file
df.to_csv('interim2.csv', index=False)

print("Modified DataFrame saved to interim2.csv")
import pandas as pd

# Read the Excel file into a pandas DataFrame
file_path = '/Users/femisokoya/Documents/GitHub/flytipping/Flytipping.xlsx'
df = pd.read_excel(file_path, sheet_name='LA_incidents', header=2)

# Replace "*Total" with "E00000000" in column 0
df.iloc[:, 1] = df.iloc[:, 1].str.replace('*Total', 'E00000000', regex=False)

# Replace "*Total" with "No relevant LA" in column 1
df.iloc[:, 2] = df.iloc[:, 2].str.replace('*Total', 'No relevant LA', regex=False)

# Delete rows 0 and 1
df = df.iloc[2:]

# Delete the last column
df = df.iloc[:, :-3]

# Delete columns with no values
df = df.dropna(axis=1, how='all')

# Save the result to CSV file
output_path = 'interim.csv'
df.to_csv(output_path, index=False)

print(f"Result saved to {output_path}")

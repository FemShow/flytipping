import pandas as pd

# Read the Excel file into a pandas DataFrame
file_path = '/Users/femisokoya/Documents/GitHub/flytipping/Flytipping.xlsx'
df = pd.read_excel(file_path, sheet_name='LA_incidents', header=2)

# Replace "*Total" with "E00000000" in column 0
# df.iloc[:, 1] = df.iloc[:, 1].str.replace('*Total', 'E00000000', regex=False)

# Replace "*Total" with "No relevant LA" in column 1
df['LA Name'] = df['LA Name'].replace('*Total', 'No Relevant LA', regex=False)

# Delete rows 0 and 1
df = df.iloc[0:]

# Delete the last column
# df = df.iloc[:, :-3]

# Delete columns with no values
# df = df.dropna(axis=1, how='all')

# Define the mapping of regions to ONS Codes
region_to_ons_code = {
    '*Total England': 'E92000001',
    '*Total England (original)':'E92000001',
    '*Total England (comparable with 2019/20)':'E92000001',
    'East Midlands': 'E12000004',
    'East': 'E12000006',
    'London': 'E12000007',
    'North East': 'E12000001',
    'North West': 'E12000002',
    'South East': 'E12000008',
    'South West': 'E12000009',
    'West Midlands': 'E12000005',
    'Yorkshire and The Humber': 'E12000003'
}

# Update the 'ONS Code' column based on the 'Region' column
df['ONS Code'] = df['Region'].map(region_to_ons_code)

# Save the modified dataframe to a new CSV file
output_path = '/Users/femisokoya/Documents/GitHub/flytipping/Flytipping_updated.csv'
df.to_csv(output_path, index=False)

print(f"Result saved to {output_path}")

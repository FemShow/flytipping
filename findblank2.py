import pandas as pd

# Read the Excel file into a pandas DataFrame
file_path = '/Users/femisokoya/Documents/GitHub/flytipping/Flytipping.xlsx'
df = pd.read_excel(file_path, sheet_name='LA_incidents', header=2)

# Drop rows 0 and 1
df = df.drop([0, 1])

# Replace "*Total" with "No relevant LA" in column 1
df['LA Name'] = df['LA Name'].replace('*Total', 'No Relevant LA', regex=False)

# Define the mapping of regions to ONS Codes
region_to_ons_code = {
    '*Total England': 'E92000001',
    '*Total England (original)': 'E92000001',
    '*Total England (comparable with 2019/20)': 'E92000001',
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

# Define the mapping of LA Name to ONS Geography codes
ons_mapping = {
    'Amber Valley': 'E07000032',
    'Ashfield': 'E07000170',
    'Babergh': 'E07000200',
    'Basildon': 'E07000065',
    'Bassetlaw': 'E07000171',
    'Bedford': 'E06000055',
    'Birmingham': 'E08000025',
    'Blaby': 'E07000129',
    'Bolsover': 'E07000033',
    'Boston': 'E07000136',
    'Braintree': 'E07000066',
    'Breckland': 'E07000143',
    'Brentwood': 'E07000067',
    'Broadland': 'E07000145',
    'Bromsgrove': 'E07000234',
    'Broxbourne': 'E07000242',
    'Broxtowe': 'E07000173',
    'Cambridge': 'E07000008',
    'Cannock Chase': 'E07000195',
    'Castle Point': 'E07000032',
    'Central Bedfordshire': 'E06000056',
    'Charnwood': 'E07000129',
    'Chelmsford': 'E07000067',
    'Chesterfield': 'E07000034',
    'Colchester': 'E07000071',
    'Coventry': 'E08000026',
    'Dacorum': 'E07000096',
    'Derby': 'E06000015',
    'Derbyshire Dales': 'E07000035',
    'Dudley': 'E08000027',
    'East Cambridgeshire': 'E07000009',
    'East Hertfordshire': 'E07000098',
    'East Lindsey': 'E07000137',
    'East Staffordshire': 'E07000195',
    'East Suffolk': 'E07000246',
    'Epping Forest': 'E07000068',
    'Erewash': 'E07000036',
    'Fenland': 'E07000010',
    'Gedling': 'E07000176',
    'Great Yarmouth': 'E07000146',
    'Harborough': 'E07000129',
    'Harlow': 'E07000069',
    'Herefordshire, County of': 'E06000019',
    'Hertsmere': 'E07000099',
    'High Peak': 'E07000037',
    'Hinckley and Bosworth': 'E07000130',
    'Huntingdonshire': 'E07000011',
    'Ipswich': 'E07000202',
    'Kings Lynn and West Norfolk': 'E07000147',
    'Leicester': 'E06000016',
    'Lichfield': 'E07000199',
    'Lincoln': 'E07000138',
    'Luton': 'E06000032',
    'Maldon': 'E07000070',
    'Malvern Hills': 'E07000235',
    'Mansfield': 'E07000177',
    'Melton': 'E07000131',
    'Mid Suffolk': 'E07000247',
    'Newark and Sherwood': 'E07000178',
    'Newcastle-under-Lyme': 'E07000194',
    'North East Derbyshire': 'E07000038',
    'North Hertfordshire': 'E07000100',
    'North Kesteven': 'E07000139',
    'North Norfolk': 'E07000148',
    'North Northamptonshire': 'E06000057',
    'North Warwickshire': 'E07000224',
    'North West Leicestershire': 'E07000132',
    'Norwich': 'E07000149',
    'Nottingham': 'E06000018',
    'Nuneaton and Bedworth': 'E07000225',
    'Oadby and Wigston': 'E07000133',
    'Peterborough': 'E06000031',
    'Redditch': 'E07000236',
    'Rochford': 'E07000072',
    'Rugby': 'E07000226',
    'Rushcliffe': 'E07000134',
    'Rutland': 'E06000017',
    'Sandwell': 'E08000028',
    'Shropshire': 'E06000051',
    'Solihull': 'E08000029',
    'South Cambridgeshire': 'E07000012',
    'South Derbyshire': 'E07000196',
    'South Holland': 'E07000135',
    'South Kesteven': 'E07000140',
    'South Norfolk': 'E07000150',
    'South Staffordshire': 'E07000198',
    'Southend-on-Sea': 'E06000033',
    'St Albans': 'E07000101',
    'Stafford': 'E07000197',
    'Staffordshire Moorlands': 'E07000192',
    'Stevenage': 'E07000242',
    'Stoke-on-Trent': 'E06000021',
    'Stratford-on-Avon': 'E07000227',
    'Tamworth': 'E07000239',
    'Telford and Wrekin': 'E06000020',
    'Tendring': 'E07000073',
    'Three Rivers': 'E07000102',
    'Thurrock': 'E06000034',
    'Uttlesford': 'E07000074',
    'Walsall': 'E08000030',
    'Warwick': 'E07000228',
    'Watford': 'E07000103',
    'Welwyn Hatfield': 'E07000104',
    'West Lindsey': 'E07000143',
    'West Northamptonshire': 'E06000066',
    'West Suffolk': 'E07000246',
    'Wolverhampton': 'E08000031',
    'Worcester': 'E06000022',
    'Wychavon': 'E07000238',
    'Wyre Forest': 'E07000239'
}

# Updates the Year column to the 'Government Year' format
df["Year"] = df["Year"].astype(str).str[:4] + "-20" + df["Year"].astype(str).str[-2:]

# Update 'ONS Code' for rows where it is blank (NaN) and 'LA Name' is in the mapping
df.loc[df['ONS Code'].isna(), 'ONS Code'] = df['LA Name'].map(ons_mapping)

# Save the updated DataFrame to a new CSV file
output_path = '/Users/femisokoya/Documents/GitHub/flytipping/Flytipping_updated2.csv'
df.to_csv(output_path, index=False)

print(f"Updated DataFrame saved to {output_path}")

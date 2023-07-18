import pandas as pd

# Read the "interim.csv" file into a pandas DataFrame
file_path = "interim.csv"
df = pd.read_csv(file_path)

# Define the id variables and value variables for melting
id_vars = ["Year", "ONS Code", "LA Name", "Region", "Total Incidents"]
value_vars = [
    "Highway Incidents", "Footpath / Bridleway Incidents", "Back Alleyway Incidents",
    "Railway Incidents", "Council Land Incidents", "Agricultural Incidents",
    "Private / Residential Incidents", "Commercial / Industrial Incidents",
    "Watercourse / Bank Incidents", "Other (unidentified) Incidents",
    "Animal Carcass Incidents", "Green Incidents", "Vehicle Parts Incidents",
    "White Goods Incidents", "Other Electrical Incidents", "Tyres Incidents",
    "Asbestos Incidents", "Clinical Incidents", "Constr / Demol / Excav Incidents",
    "Black Bags - Commercial Incidents", "Black Bags - Household Incidents",
    "Chemical Drums, Oil, Fuel Incidents", "Other Household Waste Incidents",
    "Other Commercial Waste Incidents", "Primary Waste Type Measures Other (unidentified) Incidents",
    "Single Black Bag Incidents", "Single Black Bag Clearance Costs (£)",
    "Single Item Incidents", "Single Item Clearance Costs (£)", "Car Boot or Less Incidents",
    "Car Boot or Less Clearance Costs (£)", "Small Van Load Incidents",
    "Small Van Load Clearance Costs (£)", "Transit Van Load Incidents",
    "Transit Van Load Clearance Costs (£)", "Tipper Lorry Load Incidents",
    "Tipper Lorry Load Clearance Costs (£)", "Significant / Multi Loads Incidents",
    "Sig / Multi Loads Clearance Costs (£)", "Total Incidents Clearance Costs (£)"
]
var_name = "Incidence"
value_name = "numerical"

# Melt the DataFrame
melted_df = df.melt(id_vars=id_vars, value_vars=value_vars, var_name=var_name, value_name=value_name)

# Save the melted DataFrame to "interim1.csv"
output_path = "interim1.csv"
melted_df.to_csv(output_path, index=False)

print(f"Result saved to {output_path}")

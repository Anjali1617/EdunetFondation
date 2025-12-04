import pandas as pd

# 1. Create the DataFrame using a dictionary
data = {
    "Project Name": ["SolarOne", "WindMax", "HydroFlow", "GeoDeep", "BioGen"],
    "Technology Type": ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass"],
    "Capacity (MW)": [150, 300, 500, 120, 80],
    "Cost (Million USD)": [200, 450, 700, 350, 180],
    "Location": ["California", "Texas", "Oregon", "Nevada", "Iowa"],
    "Completion Year": [2020, 2021, 2019, 2022, 2020]
}

df = pd.DataFrame(data)

# 6. Inspect DataFrame
print("Full DataFrame:")
print(df)

print("\nShape of DataFrame:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nIndex values:")
print(df.index.tolist())

# 7. Display first 3 rows and last 2 rows
print("\nFirst 3 rows:")
print(df.head(3))

print("\nLast 2 rows:")
print(df.tail(2))

# 8. Change index to 'Project Name'
df_indexed = df.set_index("Project Name")
print("\nDataFrame with 'Project Name' as index:")
print(df_indexed)

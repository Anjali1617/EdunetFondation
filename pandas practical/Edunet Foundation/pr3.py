import pandas as pd

# --- Reusing the same DataFrame from Part B ---
data = {
    "Project Name": ["SolarOne", "WindMax", "HydroFlow", "GeoDeep", "BioGen"],
    "Technology Type": ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass"],
    "Capacity (MW)": [150, 300, 500, 120, 80],
    "Cost (Million USD)": [200, 450, 700, 350, 180],
    "Location": ["California", "Texas", "Oregon", "Nevada", "Iowa"],
    "Completion Year": [2020, 2021, 2019, 2022, 2020]
}
df = pd.DataFrame(data)

# 9. Extract only "Project Name" and "Capacity (MW)"
print("Selected Columns:")
selected_cols = df[["Project Name", "Capacity (MW)"]]
print(selected_cols)

# 10. Retrieve all projects completed after year 2022
print("\nProjects completed after 2022:")
completed_after_2022 = df[df["Completion Year"] > 2022]
print(completed_after_2022)

# 11. Using loc and iloc
# Set index to project name for easy loc access
df_indexed = df.set_index("Project Name")

# 11a. Retrieve details of one specific project (e.g., 'WindMax')
print("\nDetails of project 'WindMax' using .loc:")
print(df_indexed.loc["WindMax"])

# 11b. Capacity and cost of any two projects using iloc (e.g., 1st and 3rd rows)
print("\nCapacity and Cost of two projects (using .iloc):")
two_projects = df.iloc[[0, 2]][["Capacity (MW)", "Cost (Million USD)"]]
print(two_projects)

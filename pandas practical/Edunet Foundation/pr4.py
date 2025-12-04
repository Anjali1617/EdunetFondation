import pandas as pd

# --- Reusing the same DataFrame from previous parts ---
data = {
    "Project Name": ["SolarOne", "WindMax", "HydroFlow", "GeoDeep", "BioGen"],
    "Technology Type": ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass"],
    "Capacity (MW)": [150, 300, 500, 120, 80],
    "Cost (Million USD)": [200, 450, 700, 350, 180],
    "Location": ["California", "Texas", "Oregon", "Nevada", "Iowa"],
    "Completion Year": [2020, 2021, 2019, 2022, 2020]
}
df = pd.DataFrame(data)

# 12. Filter projects with:
#    a) Capacity > 100 MW
#    b) Technology is Solar or Wind
print("Projects with capacity > 100 MW AND technology Solar/Wind:")
filtered_projects = df[
    (df["Capacity (MW)"] > 100) &
    (df["Technology Type"].isin(["Solar", "Wind"]))
]
print(filtered_projects)

# 13. Identify projects:
#    a) Located in California or Texas
#    b) Having cost > average cost
avg_cost = df["Cost (Million USD)"].mean()

print("\nProjects in California or Texas with cost greater than average:")
filtered_cost_location = df[
    (df["Location"].isin(["California", "Texas"])) &
    (df["Cost (Million USD)"] > avg_cost)
]
print(filtered_cost_location)

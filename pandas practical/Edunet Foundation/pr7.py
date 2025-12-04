import pandas as pd

# --- Reusing the same DataFrame from earlier parts ---
data = {
    "Project Name": ["SolarOne", "WindMax", "HydroFlow", "GeoDeep", "BioGen"],
    "Technology Type": ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass"],
    "Capacity (MW)": [150, 300, 500, 120, 80],
    "Cost (Million USD)": [200, 450, 700, 350, 180],
    "Location": ["California", "Texas", "Oregon", "Nevada", "Iowa"],
    "Completion Year": [2020, 2021, 2019, 2022, 2020]
}

df = pd.DataFrame(data)

# ------- 19. Grouping by Technology -------

grouped = df.groupby("Technology Type")

total_capacity_per_tech = grouped["Capacity (MW)"].sum()
avg_cost_per_tech = grouped["Cost (Million USD)"].mean()

print("=== Total Capacity per Technology ===")
print(total_capacity_per_tech)

print("\n=== Average Project Cost per Technology ===")
print(avg_cost_per_tech)

# ------- 20. Determine Highest & Lowest -------

tech_highest_capacity = total_capacity_per_tech.idxmax()
tech_lowest_avg_cost = avg_cost_per_tech.idxmin()

print("\n=== Insights ===")
print("Technology with the highest total capacity:", tech_highest_capacity)
print("Technology with the lowest average cost:", tech_lowest_avg_cost)

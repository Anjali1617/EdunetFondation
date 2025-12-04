import pandas as pd

# --- Reusing the DataFrame from earlier parts ---
data = {
    "Project Name": ["SolarOne", "WindMax", "HydroFlow", "GeoDeep", "BioGen"],
    "Technology Type": ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass"],
    "Capacity (MW)": [150, 300, 500, 120, 80],
    "Cost (Million USD)": [200, 450, 700, 350, 180],
    "Location": ["California", "Texas", "Oregon", "Nevada", "Iowa"],
    "Completion Year": [2020, 2021, 2019, 2022, 2020]
}

df = pd.DataFrame(data)

# Add cost-efficiency (Cost per MW) for analysis
df["Cost per MW"] = df["Cost (Million USD)"] / df["Capacity (MW)"]

# ------- 17. Aggregation & Statistics -------

total_capacity = df["Capacity (MW)"].sum()
total_cost = df["Cost (Million USD)"].sum()
average_capacity = df["Capacity (MW)"].mean()
max_cost = df["Cost (Million USD)"].max()
min_cost = df["Cost (Million USD)"].min()

print("=== Aggregation Results ===")
print("Total Installed Capacity:", total_capacity, "MW")
print("Total Project Cost:", total_cost, "Million USD")
print("Average Capacity:", average_capacity, "MW")
print("Maximum Project Cost:", max_cost, "Million USD")
print("Minimum Project Cost:", min_cost, "Million USD")

# ------- 18. Identify highest and lowest cost-efficiency -------

# Cost-efficiency = lower cost per MW is better
best_efficiency = df.loc[df["Cost per MW"].idxmin()]
worst_efficiency = df.loc[df["Cost per MW"].idxmax()]

print("\n=== Cost-Efficiency Analysis ===")
print("Project with highest cost-efficiency (lowest cost/MW):")
print(best_efficiency)

print("\nProject with lowest cost-efficiency (highest cost/MW):")
print(worst_efficiency)

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

# 14. Create Cost per MW column
df["Cost per MW"] = df["Cost (Million USD)"] / df["Capacity (MW)"]

# 15. Round to two decimal places
df["Cost per MW"] = df["Cost per MW"].round(2)

# 16. Add Project Size column based on capacity
def classify_size(cap):
    if cap < 100:
        return "Small"
    elif 100 <= cap <= 200:
        return "Medium"
    else:
        return "Large"

df["Project Size"] = df["Capacity (MW)"].apply(classify_size)

print(df)

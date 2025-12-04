import pandas as pd

# 1. Create a Pandas Series with renewable energy sources
sources = ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass"]

# 2. Assign custom index labels
index_labels = ["RE1", "RE2", "RE3", "RE4", "RE5"]
energy_series = pd.Series(sources, index=index_labels)

# 3a. Retrieve the first two elements using positional indexing
first_two = energy_series.iloc[:2]
print("First two elements (positional indexing):")
print(first_two)

# 3b. Retrieve the last element using label-based indexing
last_element = energy_series.loc["RE5"]
print("\nLast element (label-based indexing):")
print(last_element)

# 4. Convert the Series into a Python list
as_list = energy_series.tolist()
print("\nSeries converted to list:")
print(as_list)

# 5. Display the data type of the Series
print("\nData type of the Series:")
print(energy_series.dtype)

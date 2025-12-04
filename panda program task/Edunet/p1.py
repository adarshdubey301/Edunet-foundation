import pandas as pd

# 1. Create a Pandas Series with renewable energy sources
energy_sources = ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass"]

# 2. Assign custom index labels
index_labels = ["RE1", "RE2", "RE3", "RE4", "RE5"]
energy_series = pd.Series(energy_sources, index=index_labels)

# 3. Retrieve:
#    - First two elements using positional indexing
first_two = energy_series.iloc[:2]

#    - Last element using label-based indexing
last_element = energy_series.loc["RE5"]

# 4. Convert the Series into a Python list
energy_list = energy_series.tolist()

# 5. Check and display the data type of the Series
series_dtype = energy_series.dtype

# Output results
print("Pandas Series:\n", energy_series, "\n")
print("First two elements:\n", first_two, "\n")
print("Last element:", last_element, "\n")
print("Series converted to list:", energy_list, "\n")
print("Data type of Series:", series_dtype)

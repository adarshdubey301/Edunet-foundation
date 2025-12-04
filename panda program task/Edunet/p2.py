import pandas as pd

# 6. Create a DataFrame using a dictionary-based approach
data = {
    "Project Name": ["Solar One", "Wind Max", "Hydro Flow", "Geo Heat", "Bio Power"],
    "Technology Type": ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass"],
    "Capacity (MW)": [50, 120, 300, 80, 40],
    "Cost (Million USD)": [75, 200, 500, 150, 90],
    "Location": ["California", "Texas", "Washington", "Nevada", "Iowa"],
    "Completion Year": [2020, 2021, 2019, 2022, 2018]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:\n", df, "\n")

# Inspect shape, column names, and index values
print("Shape:", df.shape)
print("Column Names:", df.columns.tolist())
print("Index Values:", df.index.tolist(), "\n")

# 7. Display first 3 rows and last 2 rows
print("First 3 rows:\n", df.head(3), "\n")
print("Last 2 rows:\n", df.tail(2), "\n")

# 8. Change the index to the Project Name column
df_indexed = df.set_index("Project Name")
print("DataFrame with 'Project Name' as index:\n", df_indexed)

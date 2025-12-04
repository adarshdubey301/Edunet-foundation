import pandas as pd

# Sample DataFrame (same as Part B — needed for continuity)
data = {
    "Project Name": ["Solar One", "Wind Max", "Hydro Flow", "Geo Heat", "Bio Power"],
    "Technology Type": ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass"],
    "Capacity (MW)": [50, 120, 300, 80, 40],
    "Cost (Million USD)": [75, 200, 500, 150, 90],
    "Location": ["California", "Texas", "Washington", "Nevada", "Iowa"],
    "Completion Year": [2020, 2021, 2019, 2022, 2018]
}

df = pd.DataFrame(data)

# 9. Extract specific columns: Project Name and Capacity
selected_columns = df[["Project Name", "Capacity (MW)"]]
print("Selected Columns:\n", selected_columns, "\n")

# 10. Retrieve all projects completed after the year 2022
# (None exist in this dataset; using >= allows Geo Heat 2022 if needed)
completed_after_2022 = df[df["Completion Year"] > 2022]
print("Projects completed after 2022:\n", completed_after_2022, "\n")

# 11. Using .loc and .iloc
# First, set index to Project Name for easy label lookup
df = df.set_index("Project Name")

# • Retrieve details of one specific project (using .loc)
project_details = df.loc["Wind Max"]
print("Details of 'Wind Max':\n", project_details, "\n")

# • Retrieve capacity and cost of any two projects (using .iloc)
two_projects = df.iloc[1:3][["Capacity (MW)", "Cost (Million USD)"]]
print("Capacity & Cost of two projects:\n", two_projects)
 
import pandas as pd

# Sample DataFrame (same dataset as earlier parts)
data = {
    "Project Name": ["Solar One", "Wind Max", "Hydro Flow", "Geo Heat", "Bio Power"],
    "Technology Type": ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass"],
    "Capacity (MW)": [50, 120, 300, 80, 40],
    "Cost (Million USD)": [75, 200, 500, 150, 90],
    "Location": ["California", "Texas", "Washington", "Nevada", "Iowa"],
    "Completion Year": [2020, 2021, 2019, 2022, 2018]
}

df = pd.DataFrame(data)

# 12. Filter projects where:
# • Capacity > 100 MW
# • Technology is Solar or Wind

filtered_capacity = df[df["Capacity (MW)"] > 100]
print("Projects with Capacity > 100 MW:\n", filtered_capacity, "\n")

filtered_tech = df[df["Technology Type"].isin(["Solar", "Wind"])]
print("Projects with Solar or Wind Technology:\n", filtered_tech, "\n")

# 13. Identify projects:
# • Located in California or Texas
# • Having cost greater than average cost

filtered_location = df[df["Location"].isin(["California", "Texas"])]
print("Projects in California or Texas:\n", filtered_location, "\n")

avg_cost = df["Cost (Million USD)"].mean()
filtered_cost = df[df["Cost (Million USD)"] > avg_cost]
print("Projects with cost greater than average cost:\n", filtered_cost)

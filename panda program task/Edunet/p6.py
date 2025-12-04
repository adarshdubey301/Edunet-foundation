import pandas as pd

# Sample DataFrame (same as previous tasks + derived columns if needed)
data = {
    "Project Name": ["Solar One", "Wind Max", "Hydro Flow", "Geo Heat", "Bio Power"],
    "Technology Type": ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass"],
    "Capacity (MW)": [50, 120, 300, 80, 40],
    "Cost (Million USD)": [75, 200, 500, 150, 90],
    "Location": ["California", "Texas", "Washington", "Nevada", "Iowa"],
    "Completion Year": [2020, 2021, 2019, 2022, 2018]
}

df = pd.DataFrame(data)

# Add Cost per MW for cost-efficiency analysis
df["Cost per MW"] = df["Cost (Million USD)"] / df["Capacity (MW)"]

# 17. Calculations
total_capacity = df["Capacity (MW)"].sum()
total_cost = df["Cost (Million USD)"].sum()
avg_capacity = df["Capacity (MW)"].mean()
max_cost = df["Cost (Million USD)"].max()
min_cost = df["Cost (Million USD)"].min()

print("Total Installed Capacity:", total_capacity)
print("Total Project Cost:", total_cost)
print("Average Capacity:", avg_capacity)
print("Maximum Project Cost:", max_cost)
print("Minimum Project Cost:", min_cost, "\n")

# 18. Cost-efficiency (lower Cost per MW = more efficient)
best_efficiency_project = df.loc[df["Cost per MW"].idxmin()]
worst_efficiency_project = df.loc[df["Cost per MW"].idxmax()]

print("Project with Highest Cost-Efficiency (Lowest Cost per MW):\n", best_efficiency_project, "\n")
print("Project with Lowest Cost-Efficiency (Highest Cost per MW):\n", worst_efficiency_project)

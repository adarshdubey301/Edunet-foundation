import pandas as pd

# Sample DataFrame (same dataset used in earlier parts)
data = {
    "Project Name": ["Solar One", "Wind Max", "Hydro Flow", "Geo Heat", "Bio Power"],
    "Technology Type": ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass"],
    "Capacity (MW)": [50, 120, 300, 80, 40],
    "Cost (Million USD)": [75, 200, 500, 150, 90],
    "Location": ["California", "Texas", "Washington", "Nevada", "Iowa"],
    "Completion Year": [2020, 2021, 2019, 2022, 2018]
}

df = pd.DataFrame(data)

# 19. Group by Technology Type
grouped = df.groupby("Technology Type")

total_capacity_per_tech = grouped["Capacity (MW)"].sum()
avg_cost_per_tech = grouped["Cost (Million USD)"].mean()

print("Total Capacity per Technology:\n", total_capacity_per_tech, "\n")
print("Average Project Cost per Technology:\n", avg_cost_per_tech, "\n")

# 20. Determine technologies with:
# • Highest total capacity
highest_capacity_tech = total_capacity_per_tech.idxmax()
# • Lowest average cost
lowest_avg_cost_tech = avg_cost_per_tech.idxmin()

print("Technology with Highest Total Capacity:", highest_capacity_tech)
print("Technology with Lowest Average Cost:", lowest_avg_cost_tech)


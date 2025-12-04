import pandas as pd

# Sample DataFrame (same as previous tasks)
data = {
    "Project Name": ["Solar One", "Wind Max", "Hydro Flow", "Geo Heat", "Bio Power"],
    "Technology Type": ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass"],
    "Capacity (MW)": [50, 120, 300, 80, 40],
    "Cost (Million USD)": [75, 200, 500, 150, 90],
    "Location": ["California", "Texas", "Washington", "Nevada", "Iowa"],
    "Completion Year": [2020, 2021, 2019, 2022, 2018]
}

df = pd.DataFrame(data)

# 14. Create new column: Cost per MW
df["Cost per MW"] = df["Cost (Million USD)"] / df["Capacity (MW)"]

# 15. Round Cost per MW to two decimal places
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

# Display final DataFrame
print(df)

import pandas as pd

# Create a sample DataFrame
data = {'col1': [1, 2, 3, 4, 5, 6, 7, 8],
        'col2': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']}
df = pd.DataFrame(data)

# Display the first 5 rows (default behavior)
print("First 5 rows:")
print(df.head())

# Display the first 3 rows
print("\nFirst 3 rows:")
print(df.head(3))
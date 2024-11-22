import pandas as pd

data = {'Date': ['2023-01-01', '2023-02-15', '2023-02-12', '2023-03-31']}
df = pd.DataFrame(data)
print(df)
print(data)


# Converting the 'Date' column to date format
df['Date'] = pd.to_datetime(df['Date'])
print(df)

# Sorting
df = df.sort_values(by='Date')
print(f"after sorting {df}")

# Diffrent between two Date
diff = df['Date'].iloc[0] - df['Date'].iloc[1]
print(diff)  # -42 days

# Group by month and count the number of records
monthly_counts = df.groupby(df['Date'].dt.month).size()
print(monthly_counts)
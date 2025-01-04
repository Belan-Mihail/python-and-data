import pandas as pd

# Read dataset
df_sales = pd.read_csv('sales_data_with_noise.csv')

# View the first few rows of data
print('First few rows')
print(df_sales.head(10))
print('-' * 20)

# Checking data type information
print('Data type information')
print(df_sales.info())
print('-' * 20)

# Statistical description of data
print('Statistical description of data')
print(df_sales.describe())
print('-' * 20)

# Check for unique values ​​in key columns
print('Check for unique values ​​in holiday_influence')
print(df_sales['holiday_influence'].unique())
print('-' * 20)

print('Check for unique values ​​in marketing_spend')
print(df_sales['marketing_spend'].unique())
print('-' * 20)

print('Check for unique values ​​in price')
print(df_sales['price'].unique())
print('-' * 20)
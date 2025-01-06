import pandas as pd
import numpy as np

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

# Restoring the price column
def restore_price(row):
    if pd.notna(row['price_noise']):
        # If noise is added (price_noise is not NaN), restore the price
        price = row['price']
        price_noise = row['price_noise']
        
        if isinstance(price, str) and price.startswith('$'):
            # Remove the '$' symbol and convert to a number
            price = float(price[1:])
        elif isinstance(price, str):
            price = float(price)
        
        # Restore the price by dividing it by (1 + price_noise)
        restored_price = round(price / (1 + price_noise), 2)
        return restored_price
    else:
        # If noise was not added, leave the price unchanged
        return row['price']

# We restore the price only for the rows where noise was applied
df_sales['price'] = df_sales.apply(restore_price, axis=1)

# Marketing Spend Recovery
def restore_marketing_spend(spend):
    if spend == 'minimum':
        return 500
    elif spend in [np.nan, '-']:
        return 0
    try:
        return float(spend)
    except ValueError:
        return 0

df_sales['marketing_spend'] = df_sales['marketing_spend'].apply(restore_marketing_spend)

# Sales volume recovery
df_sales['sales_volume'] = round(df_sales['sales_volume'] / df_sales['sales_volume_noise'])


# Restore holiday_influence data
df_sales['holiday_influence'] = df_sales.apply(
    lambda row: 1 - row['holiday_influence'] if row['holiday_influence_noise'] else row['holiday_influence'], axis=1
)


# function to convert all month into a single format
def convert_to_standart_format(month):
    for date_format in ['%Y-%m', '%d-%m-%Y', '%b %d, %Y']:
        try:
            return pd.to_datetime(month, format=date_format).strftime('%Y-%m')
        except ValueError:
            continue
    return month

df_sales['month'] = df_sales['month'].apply(convert_to_standart_format)

# delete unnecessary columns from DF
df_sales = df_sales.drop(columns=['original_price', 'price_noise', 'sales_volume_noise', 'holiday_influence_noise'])

# Restore order by 'item_id' and 'month'
df_sales = df_sales.sort_values(by=['item_id', 'month']).reset_index(drop=True)

df_sales.to_csv('restored_sales_data.csv', index=False)
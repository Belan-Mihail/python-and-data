import pandas as pd
import numpy as np
import random

# Read dataset
df_sales = pd.read_csv('sales_data.csv')

# Shuffle the lines randomly so that the data is not in order
df_sales = df_sales.sample(frac=1, random_state=42)

# print(df_sales.head())


# Mix up the months for each product
df_sales['month'] = df_sales.groupby('item_id')['month'].transform(np.random.permutation)
print(df_sales.head())

# Entering erroneous data with a different month format
# 20% of months will be converted to the format "%d-%m-%Y"
num_rows = len(df_sales)
incorect_format_ind_1 = random.sample(range(num_rows), int(num_rows * 0.2))

for idx in incorect_format_ind_1:
    df_sales.loc[idx, 'month'] = pd.to_datetime(df_sales.loc[idx, 'month'], format='%Y-%m').strftime('%d-%m-%Y')

# 10% of months will be converted to the format "%b %d, %Y"
incorect_format_ind_2 = random.sample(range(num_rows), int(num_rows * 0.1))

for idx in incorect_format_ind_2:
    try:
        df_sales.loc[idx, 'month'] = pd.to_datetime(df_sales.loc[idx, 'month'], format='%Y-%m').strftime('%b %d, %Y')
    except ValueError:
        # If the format does not match, you can skip or handle the error
        pass

print(df_sales.head())


# Functions for "artificial corruption" of data
def add_noise_sales_volume(sales_volume):
    # add noise in range ±20%
    noise = np.random.uniform(-0.2, 0.2)
    return max(0, round(sales_volume * (1 + noise)))

def add_noise_price(price):
    noise = np.random.uniform(-0.05, 0.05)
    return round(price * (1 + noise), 2)

def add_noise_holiday_influence(holiday_influence):
    # Change holiday_influence with random probability (0 to 1 and vice versa)
    if np.random.rand() < 0.1: # 10% chance to change value
        return 1 - holiday_influence # if it was 0, it will become 1 and vice versa
    return holiday_influence

# Applying distortions to data
df_sales['sales_volume'] = df_sales['sales_volume'].apply(add_noise_sales_volume)
df_sales['price'] = df_sales['price'].apply(add_noise_price)
df_sales['holoday_influence'] = df_sales['holoday_influence'].apply(add_noise_holiday_influence)

# # To restore, we will add information about where and how the changes were made
df_sales['sales_volume_noise'] = df_sales['sales_volume'] / df_sales['sales_volume'].apply(lambda x: add_noise_sales_volume(x))

import pandas as pd
import numpy as np
import random

# Read dataset
df_sales = pd.read_csv('sales_data.csv')

# Shuffle the lines randomly so that the data is not in order
df_sales = df_sales.sample(frac=1, random_state=42)

# Mix up the months for each product
df_sales['month'] = df_sales.groupby('item_id')['month'].transform(np.random.permutation)

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

def add_noise_marketing_spend(spend):
    # With a probability of 20%, we replace the values ​​with empty, dash or "minimum"
    rand_value = np.random.rand()

    if rand_value < 0.07:
        return np.nan
    elif rand_value < 0.14:
        return '-'
    elif rand_value < 0.21:
        return 'minimum'
    else:
        return spend 

df_sales['original_price'] = df_sales['price']

# Applying distortions to data
df_sales['sales_volume'] = df_sales['sales_volume'].apply(add_noise_sales_volume)
df_sales['price'] = df_sales['price'].apply(add_noise_price)
df_sales['holiday_influence'] = df_sales['holiday_influence'].apply(add_noise_holiday_influence)
df_sales['marketing_spend'] = df_sales['marketing_spend'].apply(add_noise_marketing_spend)

# # To restore, we will add information about where and how the changes were made
df_sales['sales_volume_noise'] = df_sales['sales_volume'] / df_sales['sales_volume'].apply(lambda x: add_noise_sales_volume(x))
df_sales['price_noise'] = df_sales['price'] / df_sales['sales_volume'].apply(lambda x: add_noise_price(x))
df_sales['holiday_influence_noise'] = df_sales['holiday_influence'] != df_sales['holiday_influence'].apply(lambda x: add_noise_holiday_influence(x))

# edit format 30 % prices

np.random.seed(42)
indx_to_change = np.random.choice(df_sales.index, size=int(0.3 * len(df_sales)), replace=False)

# Change these values ​​to strings with the addition of the '$' symbol
df_sales.loc[indx_to_change, 'price'] = df_sales.loc[indx_to_change, 'price'].apply(lambda x: f"${x:.2f}")

df_sales.to_csv('sales_data_with_noise.csv', index=False)
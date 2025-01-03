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
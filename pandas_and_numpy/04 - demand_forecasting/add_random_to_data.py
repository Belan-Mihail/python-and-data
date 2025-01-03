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
incorecct_format_ind_1 = random.sample(range(num_rows), int(num_rows * 0.2))

for idx in incorecct_format_ind_1:
    df_sales.loc[idx, 'month'] = pd.to_datetime(df_sales.loc[idx, 'month'], format='%Y-%m').strftime('%d-%m-%Y')

print(df_sales.head())
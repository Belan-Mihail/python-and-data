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
# print(df_sales.head())
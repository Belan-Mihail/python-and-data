import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# loading data from csv
df = pd.read_csv("sales_data.csv")
print(df)

# Converting the 'Date' column to date format
df['Date'] = pd.to_datetime(df['Date'])
print(df)

# Which regions showed the highest sales volume over the entire period?
total_sales_by_region = df.groupby('Region')['Sales'].sum()
print(f"Analyse by region and sales summ:\n", total_sales_by_region)

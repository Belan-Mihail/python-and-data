import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# loading data from csv
df = pd.read_csv("sales_data.csv")
print(df)

# Converting the 'Date' column to date format
df['Date'] = pd.to_datetime(df['Date'])
print(df)
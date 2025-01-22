import pandas as pd
import os


print(os.getcwd())

# load data from csv
data = pd.read_csv('05 - FuelConsumption/FuelConsumption.csv', parse_dates=['Date'], dayfirst=True)

# print(data.head())

# Replace missing values ​​with 0
data['Liters'] = data['Liters'].fillna(0)
data['Cost'] = data['Cost'].fillna(0)
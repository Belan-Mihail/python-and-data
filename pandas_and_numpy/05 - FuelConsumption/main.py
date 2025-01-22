import pandas as pd
import os


print(os.getcwd())

# load data from csv
data = pd.read_csv('05 - FuelConsumption/FuelConsumption.csv', parse_dates=['Date'], dayfirst=True)

# print(data.head())

# Replace missing values ​​with 0
data['Liters'] = data['Liters'].fillna(0)
data['Cost'] = data['Cost'].fillna(0)

# Convert the column to a numeric type and replace non-numeric values ​​with NaN
data['Odo_Diff'] = pd.to_numeric(data['Odo_Diff'], errors='coerce')

# Replace Nan with 0
data['Odo_Diff'] = data['Odo_Diff'].fillna(0)

# Replace negative values ​​in the "Odo_Diff" column with 0
data['Odo_Diff'] = data['Odo_Diff'].apply(lambda x: max(0, x))

print(data.head(20))
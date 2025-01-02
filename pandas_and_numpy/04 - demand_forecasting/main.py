import pandas as pd
import numpy as np

# parameters for data generation
num_products = 10 
num_month = 6
start_date = pd.to_datetime('2024-01-01') # starting data
data_range = pd.date_range(start_date, periods=num_month, freq='ME')
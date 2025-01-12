import pandas as pd
import numpy as np
import joblib

model = joblib.load('sales_PM_GradientBoostingRegressor.pkl')

# generation data for next 2025
num_product = 10
future_data = []
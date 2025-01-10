import pandas as pd
import numpy as np
import joblib

# load model
model = joblib('sales_model.pkl')

# generation data for next 2025
num_product = 10
future_year = 2025
future_data = []
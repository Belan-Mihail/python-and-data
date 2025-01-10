import pandas as pd
import numpy as np
import joblib

# load model
model = joblib('sales_model.pkl')

# generation data for next 2025
num_product = 10
future_year = 2025
future_data = []

# generate synt data for each products for each month in next year
for item_id in range(1, num_product + 1):
    for month in range(1, 13):
        future_data.append({
            'item_id': item_id,
            'year': future_year,
            'month_number': month,
            'price': round(np.random.uniform(15, 20), 2),
            'holiday_influence': np.random.choice([0, 1], p=[0.7, 0.3]),
            'marketing_spend': round(np.random.uniform(1000, 5000), 2) 
        })
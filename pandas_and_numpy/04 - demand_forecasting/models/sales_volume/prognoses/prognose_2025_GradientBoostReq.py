import pandas as pd
import numpy as np
import joblib

model = joblib.load('sales_PM_GradientBoostingRegressor.pkl')

# generation data for next 2025
num_product = 10
future_data = []

# generate synt data for each products for each month in next year
for item_id in range(1, num_product + 1):
    for month in range(1, 13):
        future_data.append({
            'item_id': item_id,
            'month_num': month,
            'price': round(np.random.uniform(15, 20), 2),
            'holiday_influence': np.random.choice([0, 1], p=[0.7, 0.3]),
            'marketing_spend': round(np.random.uniform(1000, 5000), 2) 
        }) 

# make Dataframe from future_data
future_df = pd.DataFrame(future_data)

# make forecast
predict_sales = model.predict(future_df)

# add predicted_sales to DF
future_df['predicted_sales'] = predict_sales

# save data_frame as csv
future_df.to_csv('predicted_sales_2025_GradBootRegress.csv', index=False)
import pandas as pd
import numpy as np
import joblib

# load model
model = joblib.load('sales_model.pkl')

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

# make DataFrame 
future_df = pd.DataFrame(future_data)

# make prognose
predicted_sales = model.predict(future_df)

# add predicted_sales to DF
future_df['predicted_sales_volume'] = predicted_sales

# save data_frame as csv
future_df.to_csv('predicted_sales_2025_RandomForestRegressor.csv', index=False)


# Now, for item_id = 1, we will generate predictions for different marketing_spend values

# Initialize a list for storing the new data
future_sales_for_item = []

# We will calculate predictions for the first product (item_id = 1) across all months and for different marketing spend values
item_id = 1
marketing_spend_values = [1000, 2000, 3000, 4000, 5000]

# For each marketing spend value, generate the predictions
for marketing_spend in marketing_spend_values:
    for month in range(1, 13):  # for each month of the year
        # create a row with the same item_id and month, but different marketing_spend
        future_sales_for_item.append({
            'month_number': month,
            'marketing_spend': marketing_spend,
            'predicted_sales_volume': model.predict(pd.DataFrame([{
                'item_id': item_id,
                'year': future_year,
                'month_number': month,
                'price': round(np.random.uniform(15, 20), 2),  # price remains random
                'holiday_influence': np.random.choice([0, 1], p=[0.7, 0.3])  # holiday influence remains random
            }]))[0]  # get the prediction from the model
        })
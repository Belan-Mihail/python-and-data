import pandas as pd
import numpy as np

# parameters for data generation
num_products = 10 
num_month = 12
start_date = pd.to_datetime('2024-01-01') # starting data
data_range = pd.date_range(start_date, periods=num_month, freq='MS')

# generate data
np.random.seed(42)
data = []

# generate random data for each products
for item_id in range (1, num_products + 1):
    for month in data_range:
        # Generating random data: sales, price, and holiday/promotion influence
        sales_volume = np.random.randint(50, 500) # random sales volume
        price = round(np.random.uniform(10, 10), 2) # random price
        holiday_influence = np.random.choice([0, 1], p=[0.7, 0.3])
        seasonality = np.sin(month.month * (np.pi / 6)) * 200
        sales_volume += seasonality + (holiday_influence * 100)
        marketing_spend = round(np.random.uniform(1000, 5000), 2)
    
        data.append({
            'item_id': item_id,
            'month': month.strftime("%Y-%m"),
            'sales_volume': max(0, round(sales_volume)),
            'price': price,
            'holiday_influence': holiday_influence,
            'marketing_spend': marketing_spend
        })

sales_data = pd.DataFrame(data)

print(sales_data.head())

sales_data.to_csv('sales_data.csv', index=False)
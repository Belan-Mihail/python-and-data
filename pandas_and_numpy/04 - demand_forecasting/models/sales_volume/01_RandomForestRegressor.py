import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

df_sales = pd.read_csv('restored_sales_data.csv')

# Define features and target variable
X = df_sales[['item_id', 'month', 'price', 'holiday_influence', 'marketing_spend']]
y = df_sales['sales_volume']

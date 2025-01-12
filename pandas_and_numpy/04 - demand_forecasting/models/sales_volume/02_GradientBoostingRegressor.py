import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

# Loading cleaned data
df_sales = pd.read_csv('restored_sales_data.csv')

# Transform categorical variables
label_encoder = LabelEncoder()

# Convert 'item_id' to numeric format
df_sales['item_id'] = label_encoder.fit_transform(df_sales['item_id'])

# Fill in the missing values ​​in marketing expenses
df_sales['marketing_spend'] = df_sales['marketing_spend'].apply(pd.to_numeric, errors = 'coerce').fillna(0)

# Convert 'price' to number format (if needed)
df_sales['price'] = df_sales['price'].replace({'\$': '', ',': ''}, regex=True).astype(float)

# features and target variable
X = df_sales[['price', 'holiday_influence', 'marketing_spend', 'item_id']]
y = df_sales['sales_volume']

# training and test sample
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model initialization
model = GradientBoostingRegressor(n_estimators=100, random_state=42)


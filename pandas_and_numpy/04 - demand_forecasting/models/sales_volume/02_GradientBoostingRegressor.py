import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
import joblib

# Loading cleaned data
df_sales = pd.read_csv('restored_sales_data.csv')

# Transform categorical variables
label_encoder = LabelEncoder()

# Convert 'item_id' to numeric format
df_sales['item_id'] = label_encoder.fit_transform(df_sales['item_id'])

# Fill in the missing values ​​in marketing expenses
df_sales['marketing_spend'] = df_sales['marketing_spend'].apply(pd.to_numeric, errors = 'coerce').fillna(0)

# Convert 'price' to number format (if needed)
df_sales['price'] = df_sales['price'].replace({r'\$': '', r',': ''}, regex=True).astype(float)

# Convert the month column to datetime format
df_sales['month'] = pd.to_datetime(df_sales['month'], format='%Y-%m')

# Extract the month as a numeric attribute
df_sales['month_num'] = df_sales['month'].dt.month

# features and target variable
X = df_sales[['price', 'holiday_influence', 'marketing_spend', 'item_id', 'month_num']]
y = df_sales['sales_volume']

# training and test sample
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model initialization
model = GradientBoostingRegressor(n_estimators=100, random_state=42)

# training model
model.fit(X_train, y_train)

# forecast on test sample
y_pred = model.predict(X_test)

# model evaluation
mse = mean_squared_error(y_test, y_pred)
print(f'MSE: {mse: .2f}')

# saving model
joblib.dump(model, 'sales_PM_GradientBoostingRegressor.pkl')
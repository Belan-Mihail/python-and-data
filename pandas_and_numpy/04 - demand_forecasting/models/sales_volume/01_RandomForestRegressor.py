import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

df_sales = pd.read_csv('restored_sales_data.csv')

# Define features and target variable
X = df_sales[['item_id', 'month', 'price', 'holiday_influence', 'marketing_spend']]
y = df_sales['sales_volume']

# Divide the data into training and testing samples
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predicting on a test sample
y_pred = model.predict(X_test)
print(y_pred)
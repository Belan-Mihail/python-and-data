import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, root_mean_squared_error
from sklearn.preprocessing import StandardScaler

df_sales = pd.read_csv('restored_sales_data.csv')

# Convert 'month' to datetime type
df_sales['month'] = pd.to_datetime(df_sales['month'], format='%Y-%m')

# Extract year and month from date and add them to DataFrame as numeric features
df_sales['year'] = df_sales['month'].dt.year
df_sales['month_number'] = df_sales['month'].dt.month
df_sales = df_sales.drop(columns='month')


# Define features and target variable
X = df_sales[['item_id', 'year', 'month_number', 'price', 'holiday_influence', 'marketing_spend']]
y = df_sales['sales_volume']

# Divide the data into training and testing samples
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predicting on a test sample
y_pred = model.predict(X_test)
print(y_pred)

# Model evaluation

# Mean Square Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Square Error (MSE): {mse}")

# Root Mean Square Error (RMSE)
rmse = root_mean_squared_error(y_test, y_pred)
print(f"Root Mean Square Error (RMSE): {rmse}")

# Mean Absolute Error (MAE)
mea = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error (MEA): {mea}")

# Coefficient of determination (R²)
r2 = r2_score(y_test, y_pred)
print(f"R²: {r2}")
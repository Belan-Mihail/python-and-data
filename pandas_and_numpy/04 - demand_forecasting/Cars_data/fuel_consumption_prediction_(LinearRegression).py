import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Read dataset
df = pd.read_csv('./Cars_data/Cars.csv')

# Check column names to ensure there is no empty column
print(df.columns)

# Drop the first column (car names) since it's not a numeric feature
df = df.drop(columns=['Unnamed: 0'])

# Features (X) and target variable (y)
X = df.drop('mpg', axis=1)
y = df['mpg']

# Splitting data into training and testing samples
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model creation and training
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction on test data and evaluation
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Squared Error: {mse: .2f}")
print(f"Mean Absolute Error: {mae: .2f}")

# create a new DataFrame with 20% increased values for certain columns
df_increased = df.copy()

# Define the columns to increase by 20%
columns_to_increase = ['hp', 'disp', 'wt', 'qsec']

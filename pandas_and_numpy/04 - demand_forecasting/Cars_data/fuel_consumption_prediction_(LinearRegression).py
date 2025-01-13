import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Read dataset
df = pd.read_csv('./Cars_data/Cars.csv')

# Features (X) and target variable (y)
X = df.drop('mpg', axis=1)
y = df['mpg']


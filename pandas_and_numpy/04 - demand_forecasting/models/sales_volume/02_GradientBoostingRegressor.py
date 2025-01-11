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

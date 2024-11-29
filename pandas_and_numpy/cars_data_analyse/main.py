import pandas as pd

# 1 Loading data from Cars.csv
df = pd.read_csv('Cars.csv')
print("-" *20)

# 2 Show first 5 Line of df
print('df head \n', df.head())
print("-" *20)

# 3 print df info and description
print('df info \n', df.info)
print("-" *20)
print('df describe \n', df.describe)
print("-" *20)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# 4 сheck for missing values 
print("missing values summ: \n", df.isnull().sum())

# 5 create correlation matrix
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True)
plt.show()
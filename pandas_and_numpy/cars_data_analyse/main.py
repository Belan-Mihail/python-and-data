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
print("-" *20)

# 5 create correlation matrix
# df = df.drop('Unnamed: 0', axis=1)
# corr_matrix = df.corr()
# sns.heatmap(corr_matrix, annot=True)
# plt.show()


# 6 relationship between two variables ("mpg" and "wt")
# sns.scatterplot(x='wt', y='mpg', data=df)
# plt.show()

# 7 cars by number of cylinders and calculate average fuel consumption
cars_by_number_of_cyl_and_avar_fuel = df.groupby('cyl')['mpg'].mean()
print("cars by number of cylinders and calculate average fuel consumption \n", cars_by_number_of_cyl_and_avar_fuel)
print("-" *20)
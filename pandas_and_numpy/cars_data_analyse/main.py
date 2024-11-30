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

#8 horsepower distribution histogram
# sns.histplot(data=df, x='hp')
# plt.show()

#9 Filter cars with automatic transmission and calculate average acceleration
automatic_transmission_and_average_acceleration = df[df['am'] == 1]['qsec'].mean()
print('Filter cars with automatic transmission and calculate average acceleration \n', automatic_transmission_and_average_acceleration)
print("-" *20)

#10 "economical" and "non-economical" based on fuel consumption
df['economy'] = df['mpg'].apply(lambda x: "economic" if x > 20 else 'not economical')
print("new df \n", df.head())
print("-" *20)


# 11 fuel consumption comparison chart
# sns.boxplot(x='cyl', y='mpg', data=df)
# plt.show()

# 12 average power of 8 cylinder cars
hp8 = round(df[df['cyl'] == 8]['hp'].mean(), 2)
print("average power of 8 cylinder cars \n", hp8)
print("-" *20)

# 13 average power of 6 cylinder cars
hp6 = round(df[df['cyl'] == 6]['hp'].mean(), 2)
print("average power of 6 cylinder cars \n", hp6)
print("-" *20)

# 14 average power of 4 cylinder cars
hp4 = round(df[df['cyl'] == 4]['hp'].mean(), 2)
print("average power of 4 cylinder cars \n", hp4)
print("-" *20)

# 15 percentage of cars have automatic transmission
auto_trans = round((df['am'] == 1).mean() * 100)
print("percentage of cars have automatic transmission \n", str(auto_trans) + "%")
print("-" *20)

# 16 median weight of cars with manual transmission
med_weight_manual_trans = round(df[df['am'] == 0]['wt'].median())
print("median weight of cars with manual transmission \n", med_weight_manual_trans )
print("-" *20)

# 16  distribution of acceleration time (qsec) by categories "economy" and "not economic"
# sns.boxplot(x='economy', y='qsec', data=df)
# plt.show()


# 17 Group the cars by the number of gears and calculate the average weight for each group
avar_wt = df.groupby('gear')['wt'].mean()
print("Group the cars by the number of gears and calculate the average weight for each group \n", avar_wt)
print("-" *20)


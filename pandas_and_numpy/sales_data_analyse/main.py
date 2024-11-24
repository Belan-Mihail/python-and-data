import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1 loading data from csv
df = pd.read_csv("sales_data.csv")
# print(df)

# 2 Converting the 'Date' column to date format
df['Date'] = pd.to_datetime(df['Date'])
# print(df)

# 3 Which regions showed the highest sales volume over the entire period?
# total_sales_by_region = df.groupby('Region')['Sales'].sum()
# print(f"Analyse by region and sales summ:\n", total_sales_by_region)
# total_sales_by_region = total_sales_by_region.sort_values(ascending=False)
# print(f"Sorting by values:\n", total_sales_by_region)

# 3.1 total_sales_by_region = df.groupby('Region')['Sales'].sum()
"""
total_sales_by_region = df.groupby('Region')['Sales'].sum()
Используйте код с осторожностью.

Пошаговое объяснение:

df.groupby('Region'):

Эта часть кода группирует DataFrame df по столбцу 'Region'. Это означает, что данные в DataFrame будут сгруппированы по уникальным значениям в столбце 'Region'.
['Sales']:

После группировки, мы выбираем столбец 'Sales' для дальнейшей обработки.
.sum():

Эта функция применяется к выбранному столбцу 'Sales' для каждой группы, созданной на предыдущем шаге.
Для каждой группы она суммирует значения в столбце 'Sales'.
Что происходит в итоге:

Группировка: Данные в DataFrame группируются по регионам.
Суммирование продаж: Для каждой группы (региона) суммируются значения в столбце 'Sales'.
Сохранение результатов: Результаты суммирования сохраняются в переменной total_sales_by_region.
"""

# 4- The best month
# df["Month"] = df['Date'].dt.month
# print(df)
# monthly_sales = df.groupby('Month')['Sales'].sum()
# print("monthly sales print:", monthly_sales)
# best_month = monthly_sales.idxmax()
# print(f"Best month is {best_month}")

# 5 Most active companies
"""
.value_counts(): Этот метод подсчитывает, сколько раз каждое уникальное значение (каждая компания) встречается в выбранном столбце. Другими словами, он считает, сколько продаж было совершено каждой компанией. Результатом будет серия Pandas, где индекс - это название компании, а значение - количество продаж.
.head(5)
Этот метод выбирает первые 5 элементов из серии. В нашем случае, это будут 5 компаний с наибольшим количеством продаж.
"""
# best_companies = df['Company'].value_counts().head(5)
# print(f"Best compynies are: {best_companies}")

# 6 Monthly sales graph

# plt.figure(figsize=(8, 4))
# print("Montly sales.index", monthly_sales.index)
# print("Montly sales.values", monthly_sales.values)
# plt.plot(monthly_sales.index, monthly_sales.values)
# plt.xlabel('Month')
# plt.ylabel('Sales value')
# plt.title('Monthly sales dynamic')
# plt.show()

# 7 Average sales amount by region
# avarage_sales_by_region = df.groupby('Region')['Sales'].mean()
# min_sales_by_region = df.groupby('Region')['Sales'].min()
# print("\nMin sales by region is: ", min_sales_by_region)
# print("\nAvarage sales by region is: ", avarage_sales_by_region)


# 8 sales amount by Qatar
# min_sales_by_qatar = df.groupby('Region')['Sales'].min()['Qatar']
# print(min_sales_by_qatar, " - Qatar min")
# max_sales_by_qatar = df.groupby('Region')["Sales"].max()["Qatar"]
# print(max_sales_by_qatar, " - Qatar max")
# average_sales_in_qatar = df.groupby('Region')['Sales'].mean()['Qatar']
# print(average_sales_in_qatar, " - Qatar avg")

# 9 print head and dtypes
# print("print head \n", df.head())
# print("print dtypes\n", df.dtypes)

# 10 check missing values in df
# missing_values = df.isnull().sum()
# print(missing_values)

# 11 check df info
# print(df.info())

# 12 find strokes where sales > 1000
# df_high_sales = df[df['Sales'] > 90000]
# print("Hight sales are: ", df_high_sales)

# 13 find all companies starting with "A"
# companies_starting_with_a = df[df['Company'].str.startswith('A')]
# print("Companies starting with A", companies_starting_with_a)

# 14 find all companies starting with "d"
# companies_endig_with_d = df[df['Company'].str.endswith('d')]
# print("Companies ending with d", companies_endig_with_d)

# 15 find all companies contain "so"
# companies_contain_soft = df[df['Company'].str.contains('so')]
# print("so companis: ", companies_contain_soft)

# 16 find all companis with long name
# companies_with_long_name = df[df['Company'].str.len() > 30]
# print("Long name companies", companies_with_long_name)

# 17 find all companies starting with a case insensitive
# companies_with_a = df[df["Company"].str.lower().str.startswith('a')]
# print('Companies starting with a', companies_with_a)

# 18 find all companies starting with L and ending with d
# compines_starting_with_l_and_ending_with_d = df[(df['Company'].str.startswith('L')) & (df['Company'].str.endswith('d'))]
# print("Companies: ", compines_starting_with_l_and_ending_with_d)

# 19 all companies from Qatar
# companies_from_qatar = df[df['Region'] == 'Qatar']
# qatar_companies_list = companies_from_qatar['Company'].to_list()
# print(companies_from_qatar)
# print(qatar_companies_list)

# 20 unique companies and region
print(df['Company'].unique)
print(df['Region'].unique)

# у меня есть сsv файл с такими колонками (Name,Region,Company,Date,Sales) со 100 строками данных. 
# у меня есть сsv файл с такими колонками (Name,Region,Company,Date,Sales) со 100 строками данных. мне нужны задания средней сложности с данными которые содержаться в этом файле по пайтон пандас и матлиб для тренировки с решением, чтоб я мог свериться   
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
total_sales_by_region = df.groupby('Region')['Sales'].sum()
# print(f"Analyse by region and sales summ:\n", total_sales_by_region)
total_sales_by_region = total_sales_by_region.sort_values(ascending=False)
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
df["Month"] = df['Date'].dt.month
print(df)
monthly_sales = df.groupby('Month')['Sales'].sum()
print(monthly_sales)
best_month = monthly_sales.idxmax()
print(f"Best month is {best_month}")


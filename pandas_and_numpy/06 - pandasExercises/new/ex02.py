# Ex2 - Getting and Knowing your Data
# This time we are going to pull data directly from the internet. Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.

# Step 1. Import the necessary libraries
import pandas as pd
 
# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called chipo.
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep='\t')
 
# Step 4. See the first 10 entries
print(chipo.head(10))
 
# Step 5. What is the number of observations in the dataset?
print(chipo.shape[0])
# 4622

# Step 6. What is the number of columns in the dataset?
print(chipo.shape[1])
# 5
 
# Step 7. Print the name of all the columns.
print(chipo.columns)
 
# Step 8. How is the dataset indexed?
print(chipo.index)
 
# Step 9. Which was the most-ordered item?
most_ordered_item = chipo.groupby('item_name').sum()['quantity'].idxmax()
print(most_ordered_item)
# Chicken Bowl

# Step 10. For the most-ordered item, how many items were ordered?
most_ordered_item_quantity = chipo.groupby('item_name').sum()['quantity'].max()
print(most_ordered_item_quantity)
 
# Step 11. What was the most ordered item in the choice_description column?
most_ordered_choice_description = chipo.groupby('choice_description').value_counts().idxmax()
print(most_ordered_choice_description)
 
# Step 12. How many items were orderd in total?
total_item_oders = chipo['quantity'].sum()
print(total_item_oders)
 
# Step 13. Turn the item price into a float
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))
# Step 13.a. Check the item price type
print(chipo['item_price'].dtype)
 
 
# Step 14. How much was the revenue for the period in the dataset?
chipo['revenue'] = chipo['item_price'] * chipo['quantity']
total_revenue = chipo['revenue'].sum()
print(total_revenue)
# 39237.02
 
# Step 15. How many orders were made in the period?
total_orders = chipo['order_id'].nunique()
print(total_item_oders)
 
# Step 16. What is the average revenue amount per order?
average_revenue_per_order = total_revenue / total_orders
print(average_revenue_per_order)

# Step 17. How many different items are sold?
unique_items_sold = chipo['item_name'].nunique()
print(unique_items_sold)
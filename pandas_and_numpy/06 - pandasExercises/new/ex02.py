# Ex2 - Getting and Knowing your Data
# This time we are going to pull data directly from the internet. Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.

# Step 1. Import the necessary libraries
import pandas as pd
 
# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called chipo.
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep='\t')
 
# Step 4. See the first 10 entries
 
# Step 5. What is the number of observations in the dataset?
# # Solution 1
# # Solution 2
# Step 6. What is the number of columns in the dataset?
 
# Step 7. Print the name of all the columns.
 
# Step 8. How is the dataset indexed?
 
# Step 9. Which was the most-ordered item?
 
# Step 10. For the most-ordered item, how many items were ordered?
 
# Step 11. What was the most ordered item in the choice_description column?
 
# Step 12. How many items were orderd in total?
 
# Step 13. Turn the item price into a float
# Step 13.a. Check the item price type
 
# Step 13.b. Create a lambda function and change the type of item price
 
# Step 13.c. Check the item price type
 
# Step 14. How much was the revenue for the period in the dataset?
 
# Step 15. How many orders were made in the period?
 
# Step 16. What is the average revenue amount per order?
# # Solution 1
# # Solution 2
# Step 17. How many different items are sold?
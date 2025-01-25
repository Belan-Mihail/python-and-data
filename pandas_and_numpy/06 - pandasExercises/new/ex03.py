# Ex3 - Getting and Knowing your Data
# This time we are going to pull data directly from the internet. Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.

# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
 
# Step 2. Import the dataset from this address.
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'


# Step 3. Assign it to a variable called users and use the 'user_id' as index
users = pd.read_csv(url, index_col='user_id', sep='|', encoding='utf-8')
 
# Step 4. See the first 25 entries
print(users.head(25))
 
# Step 5. See the last 10 entries
print(users.tail(10))
 
# Step 6. What is the number of observations in the dataset?
print(users.shape[0])
 
# Step 7. What is the number of columns in the dataset?
print(users.shape[1])
 
# Step 8. Print the name of all the columns.
 
# Step 9. How is the dataset indexed?
 
# Step 10. What is the data type of each column?
 
# Step 11. Print only the occupation column
 
# Step 12. How many different occupations are in this dataset?
 
# Step 13. What is the most frequent occupation?
 
# Step 14. Summarize the DataFrame.
 
# Step 15. Summarize all the columns
 
# Step 16. Summarize only the occupation column
 
# Step 17. What is the mean age of users?
 
# Step 18. What is the age with least occurrence?
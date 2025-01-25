# Exercise 1
# Step 1. Go to https://www.kaggle.com/openfoodfacts/world-food-facts/data
# Step 2. Download the dataset to your computer and unzip it.
# Step 3. Use the tsv file and assign it to a dataframe called food
import pandas as pd
import os


current_directory = os.getcwd() 
print(current_directory)
food = pd.read_csv('06 - pandasExercises/new/04/en.openfoodfacts.org.products.tsv', sep='\t')

# Step 4. See the first 5 entries
print(food.head())
 
# Step 5. What is the number of observations in the dataset?
print(food.shape)
 
# Step 6. What is the number of columns in the dataset?
print(food.shape[1])
 
# Step 7. Print the name of all the columns.
print(food.columns)
 
# Step 8. What is the name of 105th column?
 
# Step 9. What is the type of the observations of the 105th column?
 
# Step 10. How is the dataset indexed?
 
# Step 11. What is the product name of the 19th observation?
import numpy as np


# 9 Adding two NumPy arrays of the same size
array1 = np.array([[1,2,3], [4,5,6]])
array2 = np.array([[7,8,9], [10,11,12]])
result = array1 + array2
print("N9 result\n", result)

# 8 Change all items in the third column to 10. 8.1 Changing multiple columns. 8.2 Changing elements by condition
# 8.3 Modifying Elements with Functions
new_array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
new_array1[:, 2] = 10
print("N8 new_array1\n", new_array1)
print("-" * 20)
new_array1[:, 1:3] = 11
print("N8.1 new_array1\n", new_array1)
print("-" * 20)
new_array1[new_array1 < 5 ] = 8
print("N8.2 new_array1\n", new_array1)
print("-" * 20)
new_array2 = new_array1[2, :] * 2
print("N8.3 new_array2\n", new_array2)
print("N8.3 new_array1\n", new_array1)
print("-" * 20)


# 7 (7.1) Extract elements from array with step 2
new_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sub_array = new_array[1:3, 1:3]
print("N7.2 sub_array\n", sub_array)
print("-" * 20)
second_row = new_array[1, :]
print("N7.1 second row\n", second_row)
print("-" * 20)
third_column = new_array[:, 2]
print("N7 third column\n", third_column)
print("-" * 20)

# 6 Extract elements from array with step 2
array_from_5_to_20 = np.arange(5,21)
arr_elements_step_2 = array_from_5_to_20[::2]
print("N6\n", arr_elements_step_2)
print("-" * 20)

# 5 Extract from 2 to 4 elements
el_from_2_to_4 = array_from_5_to_20[1:4]
print("N5\n", el_from_2_to_4)
print("-" * 20)


# 4. Extract the first 5 elements
first_five_el = array_from_5_to_20[:5]
print("N4\n", first_five_el)
print("-" * 20)

# 3.1 Create an array with step 2.
array_with_step_2 = np.arange(5,16,2)
print("N3.1\n", array_with_step_2)
print("-" * 20)

# 3 Create an array of 10 consecutive numbers from 5 to 15.
array_from_5_to_15 = np.arange(5,16)
print("N3\n", array_from_5_to_15)
print("-" * 20)

# 2.1 Create a 3x4 array filled with 7
sevens_array = np.full((3,4), 7)
print("N2.1 ", sevens_array)
print("-" * 20)

# 2 Create a 5x5 array filled with zeros
zero_array = np.zeros((5,5))
print("N2\n", zero_array)
print("-" * 20)

# 1 Create an array of 10 random integers in the range 0 to 10
random_array = np.random.randint(0, 11, size=10)
print("N1\n", random_array)
print("-" * 20)



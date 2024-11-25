import numpy as np


# 1 Create an array of 10 random integers in the range 0 to 10
random_array = np.random.randint(0, 11, size=10)
print(random_array)
print("-" * 20)


# 2 Create a 5x5 array filled with zeros
zero_array = np.zeros((5,5))
print(zero_array)
print("-" * 20)

# 2.1 Create a 3x4 array filled with 7
sevens_array = np.full((3,4), 7)
print(sevens_array)
print("-" * 20)

# 3 Create an array of 10 consecutive numbers from 5 to 15.
array_from_5_to_15 = np.arange(5,16)
print(array_from_5_to_15)
print("-" * 20)
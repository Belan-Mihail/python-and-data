# Given, two Series bees and knees, if the ith value of bees is NaN, double the ith value inside knees.

import numpy as np
import pandas as pd

bees = pd.Series([True, True, False, np.nan, True, False, True, np.nan])
knees = pd.Series([5,2,9,1,3,10,5,2], index = [7,0,2,6,3,5,1,4])

print(bees)
# 0     True
# 1     True
# 2    False
# 3      NaN
# 4     True
# 5    False
# 6     True
# 7      NaN
# dtype: object

print(knees)
# 7     5
# 0     2
# 2     9
# 6     1  <-- double this
# 3     3
# 5    10
# 1     5
# 4     2  <-- double this
# dtype: int64


# Given a Series of car asking_prices and another Series of car fair_prices, determine which cars for sale are a good deal.
#  In other words, identify cars whose asking price is less than their fair price.

import numpy as np
import pandas as pd

asking_prices = pd.Series([5000, 7600, 9000, 8500, 7000], index=['civic', 'civic', 'camry', 'mustang', 'mustang'])
fair_prices = pd.Series([5500, 7500, 7500], index=['civic', 'mustang', 'camry'])

print(asking_prices)
# civic      5000
# civic      7600
# camry      9000
# mustang    8500
# mustang    7000
# dtype: int64

print(fair_prices)
# civic      5500
# mustang    7500
# camry      7500
# dtype: int64
# The result should be a list of integer indices corresponding to the good deals in asking_prices.
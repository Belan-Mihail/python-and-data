
# You and your spouse decided to let the internet name your next child. 
# You’ve asked the great people of the web to submit their favorite names, 
# and you’ve compiled their submissions into a Series called babynames.

import numpy as np
import pandas as pd

babynames = pd.Series([
    'Jathonathon', 'Zeltron', 'Ruger', 'Phreddy', 'Ruger', 'Chad', 'Chad',
    'Ruger', 'Ryan', 'Ruger', 'Chad', 'Ryan', 'Phreddy', 'Phreddy', 'Phreddy',
    'Mister', 'Zeltron', 'Ryan', 'Ruger', 'Ruger', 'Jathonathon',
    'Jathonathon', 'Ruger', 'Chad', 'Zeltron'], dtype='string')

# !Task
# Determine how many people voted for the names ‘Chad’, ‘Ruger’, and ‘Zeltron’.
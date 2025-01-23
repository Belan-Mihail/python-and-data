
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

name_counts = babynames.value_counts()

chad_count = name_counts.get('Chad', 0)
ruger_count = name_counts.get('Ruger', 0)
zelton_count = name_counts.get('Zeltron', 0)

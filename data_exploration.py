# Import cleaned dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

trees = pd.read_csv("trees_cleaned.csv")

# CHANGE INT64 DATA TYPES TO DATETIME
'''More convenient for visualizations later on'''
trees['load_date'] = pd.to_datetime(trees['load_date'].astype(str), format='%Y-%m-%d')
trees['updated'] = pd.to_datetime(trees['updated'].astype(str), format='%Y-%m-%d')

'''
What is the distribution of the different species of trees?
What is the distribution of the different ages of trees?
According to their species and age, what trees are likely to wilt/die soon?
Where are new trees being planted (geographically)?
Based on their age, when are the trees due for pruning?'''

# SPECIES MAP
species_map = sb.FacetGrid(data=trees, hue='tree_name')
plt.xticks(np.arange(min(trees['longitude']), max(trees['longitude'])+0.1, 0.001))
# plt.yticks(np.arange(min(trees['latitude']), max(trees['latitude'])+0.1, 0.001))

species_map.map(plt.scatter, 'longitude', 'latitude', s=0.0001).add_legend()
plt.show()

# SPECIES BAR GRAPH

# AGE MAP

# AGE BAR GRAPH

# TREES DUE FOR PRUNING THIS YEAR
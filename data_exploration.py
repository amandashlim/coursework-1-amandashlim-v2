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

# MAP BY SPECIES
species_map = sb.FacetGrid(data=trees, hue='tree_name')
species_map.map(plt.scatter, 'longitude', 'latitude', s=0.0005)
plt.title("Map of London Trees by Species")
plt.legend(markerscale=100, fontsize=3, title="Species of Tree")
plt.show()

# BAR GRAPH BY SPECIES COUNT

# MAP BY AGE

# BAR GRAPH BY AGE

# TREES DUE FOR PRUNING THIS YEAR
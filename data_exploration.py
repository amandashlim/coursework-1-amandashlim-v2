# Write code that explores your data set
# Import dataset
import pandas as pd
trees = pd.read_csv (r'/Users/amandashlim/Downloads/cw1/Borough_tree_list_2021July.csv')
print (trees)

# Explore values and value counts in pandas
trees.info()
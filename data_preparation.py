import pandas as pd

# Load excel file into pandas dataframe
# Data from https://data.london.gov.uk/dataset/local-authority-maintained-trees
trees = pd.read_excel("Borough_tree_list_2021July.xlsx")

# Investigate data attributes
# Rows and columns
print(trees.shape)
print(trees.head())
print(trees.columns)
print(trees.info(verbose=True))

# Remove unecessary columns

# Fill in missing values where possible

# Omit rows with too little data
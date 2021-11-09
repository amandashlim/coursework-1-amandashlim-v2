# LOAD DATA INTO PANDAS DATAFRAME ---
import pandas as pd

# Data from https://data.london.gov.uk/dataset/local-authority-maintained-trees
# May need to pip install openpyxl
# Needed to use excel format since could not upload .csv to GitHub due to file size
trees_nonprep = pd.read_excel("Borough_tree_list_2021July.xlsx")

# INVESTIGATE ROWS AND COLUMNS ---
print(trees_nonprep.shape)
print(trees_nonprep.head())
print(trees_nonprep.columns)
print(trees_nonprep.info(verbose=True))

# REMOVE UNECESSASRY COLUMNS ---
# Drop less relevant columns or columns with repeated information and little data
'''
diameter_at_breast_height_cm are not relevant to planting or maintenance.
dbh_group has <19k entries while the entire dataset has >817k.
canopy_spread_group has <19k entries and spread_m has more data.
kept age_group since still convenient for data visualization purposes even though information is repeated.'''
trees = trees_nonprep.drop(['diameter_at_breast_height_cm', 'dbh_group', 'canopy_spread_group'], axis=1)

# FILL IN MISSING VALUES FOR TREE_NAME ---
# Check difference between gla_tree_name, tree_name, and taxon name
trees_nonprep['gla_tree_name'].unique()
trees_nonprep['tree_name'].unique()
trees_nonprep['taxon_name'].unique()
trees_nonprep['common_name'].unique()

'''Can we fill in the missing tree value names with the names in other columns?
tree_name has the most values and so we should try and fill in the missing tree_name's.'''

# Find what rows have no tree_name. We only care about the tree name columns so omit all other ones.
all_tree_names = trees[['gla_tree_name', 'tree_name', 'taxon_name', 'common_name']]
tree_name_na = all_tree_names[all_tree_names['tree_name'].isna()]

# May need to run pd.set_option("display.max_rows", None, "display.max_columns", None)
tree_name_na

'''It seems like whenever the tree_name is NA, the gla_tree_name is Other. Check to confirm.'''
tree_name_na['gla_tree_name'].unique()
tree_name_na['tree_name'].unique()

'''Now we know this is true. We also know that for all rows where tree_name is NA, there are values for
taxon_name and common_name. Since common_name is easier to read/understand, we can replace all missing values for
tree_name with their corresponding common_name.'''

# Replace missing values for tree_name with common_name
trees['tree_name'] = trees['tree_name'].fillna(value=trees['common_name'])

# Check if any NA's are left
trees['tree_name'].isna().unique()
'''Returns all false so we successfully replaced all NA's'''

# Remove all tree naming columns except tree_name
trees = trees.drop(['gla_tree_name', 'taxon_name', 'common_name'], axis=1)

# CHECK FOR AND REMOVE DUPLICATES
print(trees.duplicated().unique())
'''There are no duplicate rows.'''

# EXPORT DATASET ---
# Check out new cleaned dataset
trees.info()

# Export dataset to csv
trees.to_csv("trees_cleaned.csv", index=False)
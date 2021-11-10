# Import cleaned dataset
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

# PIE GRAPH BY SPECIES COUNT
species_series = trees['tree_name'].value_counts(normalize=True)
species_percentages = pd.DataFrame({'tree_name':species_series.index, 'percentage':species_series.values})

# Aggregate percentages for all the species that have a percentage of less than 0.02
# category into one "Other Species" category
other_agg_percent = species_percentages[species_percentages['percentage'] < 0.02].sum(axis=0).iloc[1]

# Remove individual rows for species with percentage less than 0.02 from the dataframe
species_percentages = species_percentages[species_percentages['percentage'] >= 0.02]

# Append Other Species row to end of dataframe
species_percentages.loc[len(species_percentages)] = ["Various Species", other_agg_percent]

# Plot pie chart
species_pie = plt.pie(species_percentages['percentage'], labels=species_percentages['tree_name'], autopct='%1.1f%%')
plt.title("Percentages of Tree Species in London Boroughs")
plt.show()

# MAP BY AGE
age_map = sb.FacetGrid(data=trees, hue='age_group')
age_map.map(plt.scatter, 'longitude', 'latitude', s=0.0005)
plt.title("Map of London Borough Trees by Age Group")
plt.legend(markerscale=300, title="Age of Tree")
plt.show()

# BAR GRAPH BY AGE
age_bar = trees.age_group.value_counts().plot(kind="barh")
plt.title("Count of Trees in London Boroughs by Age Group")
plt.xlabel("Number of Trees")
plt.show()

# TREES PLANTED OVER TIME

# TREES DUE FOR PRUNING THIS YEAR
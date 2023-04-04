# Open data set and filter it using pandas, then save it as a new file

import pandas as pd

# Read in the data set
df = pd.read_csv('raw-data.csv', index_col=0, encoding='latin-1')
#print(df.shape)
#print first 5 rows only 'article_title'
#print(df['article_title'].head())
filters= ['biologia','ciências biológicas','bióloga','biólogo']

# filter the data set to only include rows where at least one item of the 'filters' are found in column 'abstract 
df_filtered = df[df['abstract'].str.contains('|'.join(filters))]

# show the first 5 rows of the filtered data set
#print(df_filtered.head())

# count the number of rows in the filtered data set
#print(df_filtered.shape)

# save column 'article_category' and 'article_title' of the filtered data set
df_filtered = df_filtered[['article_category','article_title']]

# save the filtered data set as a new file
df_filtered.to_csv('filtered-data.csv')
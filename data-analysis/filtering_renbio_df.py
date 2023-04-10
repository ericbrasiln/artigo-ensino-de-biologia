# Open data set and filter it using pandas, then save it as a new file

import pandas as pd

# Read in the data set
df = pd.read_csv("renbio.csv")

print(df.shape)
print(df["pub_date"].value_counts())


filters = [
    "educação crítica",
    "ensino crítico",
    "ensino problematizador",
    "anti-racista*",
    "antirracista*",
    "relações étnico-raciais",
    "étnico*",
    "anti-sexista",
    "raça",
    "racismo*",
    "racial*",
    "gênero",
    "transgêner*",
    "feminismo*",
]

# filter the data set to only include rows where at least one item of the 'filters' are found in column 'abstract
df_filtered = df[df["abstract"].str.contains("|".join(filters))]

# count the number of rows in the filtered data set
print(df_filtered.shape)

# save the filtered data set as a new file
df_filtered.to_csv("renbion-filtered-data.csv")

# count items in column 'pub_date'
print(df_filtered["pub_date"].value_counts())

# calculate the percentage of articles per year
print(df_filtered["pub_date"].value_counts(normalize=True))

# count words in abstracts, only if the word is longer than 3 characters
# exclude words that are shorter than 3 characters
# save the word count as a new file
df_filtered["abstract"].str.split(expand=True).stack().value_counts().loc[
    lambda x: x.index.str.len() > 3
].to_csv("renbio-word-count.csv")

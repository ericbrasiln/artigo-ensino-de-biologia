# Open data set and filter it using pandas, then save it as a new file

import pandas as pd
import plotly.express as px

# Read in the data set
df = pd.read_csv("raw-data.csv", index_col=0)
# print(df.shape)
# print first 5 rows only 'article_title'
# print(df['article_title'].head())

filters = ["biologia", "ciências biológicas", "bióloga*", "biólogo*"]
f_humanas = [
    "ciências humanas",
    "antropologia",
    "antropólog*",
    "cientista social",
    "ciência social",
    "ciências sociais",
    "história",
    "historiador*",
    "sociologia",
    "sociólog*",
]
f_antr = ["antropologia", "antropólog*"]
f_cien_soc = ["cientista* socia*", "ciência social", "ciências sociais"]
f_hist = ["história", "historiador*"]
f_soci = ["sociologia", "sociólog*"]

# filter the data set to only include rows where at least one item of the 'filters' are found in column 'abstract
df_filtered = df[df["abstract"].str.contains("|".join(filters))]
df_humanas = df[df["abstract"].str.contains("|".join(f_humanas))]
df_antr = df[df["abstract"].str.contains("|".join(f_antr))]
df_cien_soc = df[df["abstract"].str.contains("|".join(f_cien_soc))]
df_hist = df[df["abstract"].str.contains("|".join(f_hist))]
df_soci = df[df["abstract"].str.contains("|".join(f_soci))]

# count the number of rows in the filtered data set
print(df_filtered.shape)
print(df_humanas.shape)
print(df_antr.shape)
print(df_cien_soc.shape)
print(df_hist.shape)
print(df_soci.shape)

# save the filtered data set as a new file
df_filtered.to_csv("filtered-data.csv")

# count items in column 'pub_date'
print(df_filtered["pub_date"].value_counts())

# count items in column 'journal_title'
print(df_filtered["journal_title"].value_counts())

# count items in column 'article_category'
print(df_filtered["article_category"].value_counts())

# create a df with 'refs' column
df_refs = df_filtered["refs"]

# count words in abstracts, only if the word is longer than 3 characters
# exclude words that are shorter than 3 characters
print(
    df_filtered["abstract"]
    .str.split(expand=True)
    .stack()
    .value_counts()
    .loc[lambda x: x.index.str.len() > 3]
)

# save the word count as a new file
df_filtered["abstract"].str.split(expand=True).stack().value_counts().loc[
    lambda x: x.index.str.len() > 3
].to_csv("word-count.csv")

# create a graph with df_filtered['pub_date'].value_counts() and df['pub_date'].value_counts()
# save the graph as a new file
fig = px.bar(
    df_filtered["pub_date"].value_counts(),
    x=df_filtered["pub_date"].value_counts().index,
    y=df_filtered["pub_date"].value_counts().values,
    title="Publications per year",
)
fig.write_html("publications-per-year.html")
# show fig
fig.show()

# create a graph with df_filtered['journal_title'].value_counts() and df['journal_title'].value_counts()
# save the graph as a new file
fig = px.bar(
    df_filtered["journal_title"].value_counts(),
    x=df_filtered["journal_title"].value_counts().index,
    y=df_filtered["journal_title"].value_counts().values,
    title="Publications per journal",
)
fig.write_html("publications-per-journal.html")
# show fig
fig.show()

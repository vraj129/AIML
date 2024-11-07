import pandas as pd

df = pd.read_csv("path to file")
# print(df.head(3))
# print(df.industry.unique())
# print(df.language.value_counts())
# print(df[["title","release_year"]])
# print(df[(df.release_year >= 2000) & (df.release_year <= 2010)])
# print(df.describe())
# print(df[(df.imdb_rating == df.imdb_rating.max()) | (df.imdb_rating == df.imdb_rating.min())])

df["age"] = df["release_year"].apply(lambda x: 2023 - x)
print(df)
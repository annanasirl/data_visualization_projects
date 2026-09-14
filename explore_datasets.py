import pandas as pd

movies = pd.read_csv('data/raw/movies_metadata.csv')

print(movies.head())
print(movies.columns)
print(movies.shape)

print(movies.info())
print(movies.isna().sum())
print(movies.dtypes)

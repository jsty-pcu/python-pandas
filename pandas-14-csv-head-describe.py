import pandas as pd

df = pd.read_csv('pokemon.csv', index_col=0, encoding='ISO-8859-1')

print(df.head())

print("-------------------")

print(df.describe())
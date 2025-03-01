import pandas as pd

df = pd.read_csv('pokemon.csv', index_col=0, encoding='ISO-8859-1')
print(df.head())
stats_df = df.drop(['Total', 'Generation', 'Legendary'], axis=1)
melted_df = pd.melt(stats_df, id_vars=["Name", "Type1", "Type2"], var_name="Stat")

print(melted_df.head())
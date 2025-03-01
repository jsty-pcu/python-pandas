import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('pokemon.csv', index_col=0, encoding='ISO-8859-1')

bin_edges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
g = plt.hist(df['Speed'], histtype='bar', ec='black', bins=bin_edges)
g = plt.xlabel('Pokemon Speed')
g = plt.ylabel('Frequesncy')

plt.show()
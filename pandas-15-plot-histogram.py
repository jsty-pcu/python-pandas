import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('pokemon.csv', index_col=0, encoding='ISO-8859-1')

g = plt.hist(df['Speed'], histtype='bar', ec='black')
g = plt.xlabel('Pokemon Speed')
g = plt.ylabel('Frequesncy')

plt.show()
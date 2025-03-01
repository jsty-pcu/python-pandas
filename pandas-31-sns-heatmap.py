import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('pokemon.csv', index_col=0, encoding='ISO-8859-1')
stats_df = df.drop(['Name', 'Type1', 'Type2', 'Total', 'Generation', 'Legendary'], axis=1)

corr = stats_df.corr()

sns.heatmap(corr)
plt.show()
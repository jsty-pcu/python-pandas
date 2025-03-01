import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('pokemon.csv', index_col=0, encoding='ISO-8859-1')

sns.set_style()
sns.lmplot(x='Attack', y='Defense', data=df, fit_reg=False)

plt.show()
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('pokemon.csv', index_col=0, encoding='ISO-8859-1')
type_colors = [
    "#7AC74C", # Grass
    "#EE8130", # Fire
    "#6390F0", # Water
    "#A6B91A", # Bug
    "#A8A77A", # Normal
    "#A33EA1", # Poison
    "#F7D02C", # Electric
    "#E2BF65", # Ground
    "#D685AD", # Fairy
    "#C22E28", # Fighting
    "#F95587", # Psychic
    "#B6A136", # Rock
    "#735797", # Ghost
    "#96D9D6", # Ice
    "#6F35FC", # Dragon
    "#705746", # Dark
    "#B7B7CE", # Steel
    "#A98FF3", # Flying
]

sns.set_style()
sns.swarmplot(x='Type1', y='Attack', data=df, palette=type_colors)

plt.show()
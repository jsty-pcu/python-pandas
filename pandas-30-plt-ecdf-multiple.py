import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('pokemon.csv', index_col=0, encoding='ISO-8859-1')
stats_df = df.drop(['Total', 'Generation', 'Legendary'], axis=1)
melted_df = pd.melt(stats_df, id_vars=["Name", "Type1", "Type2"], var_name="Stat")

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

x_attack = np.sort(df['Attack'])
x_defense = np.sort(df['Defense'])
x_speed = np.sort(df['Speed'])

y_attack = np.arange(1, len(x_attack) + 1) / len(x_attack)
y_defense = np.arange(1, len(x_defense) + 1) / len(x_defense)
y_speed = np.arange(1, len(x_speed) + 1) / len(x_speed)

plt.plot(x_attack, y_attack, marker='.', linestyle='none', label="Attack")
plt.plot(x_defense, y_defense, marker='.', linestyle='none', label="Defense")
plt.plot(x_speed, y_speed, marker='.', linestyle='none', label="Speed")

plt.xlabel('Stats')
plt.ylabel('ECDF')

plt.margins(0.02)
plt.legend()
plt.show()
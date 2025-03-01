import pandas as pd

df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628],
}, index=['KZ', 'RU', 'BY', 'UA'])

print(df[df.population > 10][['country', 'square']])

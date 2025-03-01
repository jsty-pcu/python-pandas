import pandas as pd

list2 = [[0, 1, 2], [3, 4, 5], [6, 7, 8],]

df = pd.DataFrame(list2)

print(df)

df.columns = ['V1', 'V2', 'V3']

print(df)
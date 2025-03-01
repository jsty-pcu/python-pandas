import pandas as pd

new_series = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(new_series.values)
print('_____________')
new_series[['a', 'b', 'f']] = 0
print(new_series)
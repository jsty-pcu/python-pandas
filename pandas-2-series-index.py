import pandas as pd

new_series = pd.Series([5, 6, 7, 8, 9, 10])
print(new_series.values)
print('_____________')
print(new_series[4])


print('\n\n\n')

new_series = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(new_series.values)
print('_____________')
print(new_series['f'])
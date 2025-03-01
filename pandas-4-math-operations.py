import pandas as pd

new_series = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
new_series2 = new_series[new_series > 0]
print(new_series2)
print('_____________')
new_series2[new_series2 > 0] * 2
print(new_series2)
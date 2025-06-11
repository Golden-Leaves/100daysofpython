import pandas as pd
from datetime import datetime

# Time series data
dates = pd.date_range(start='20200101', periods=4)
values = [10, 20, -10, 5]

df = pd.DataFrame({'Values': values}, index=dates)
cumulative_sum = df['Values'].cumsum()
print(cumulative_sum)
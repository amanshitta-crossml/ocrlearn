import numpy as np
import pandas as pd
import pdb
# Data frame
df = pd.read_csv('CSV/smallbig.csv')

rows, columns = df.shape
print(rows, columns)
print(df.describe())
series_mag = df[['Industry_name_NZSIOC','Units','Variable_name']]
# print(series_mag.head(rows-120))

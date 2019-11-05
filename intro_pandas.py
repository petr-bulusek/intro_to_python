# -*- coding: utf-8 -*-
"""
@author: petr bulusek
"""

# pandas
# built on top of numpy


import pandas as pd

# pd.read_csv
# pd.read_excel
# ...

df = pd.read_csv('survey.csv')

df.info()
df.describe()

df.index
df.columns

df = df.set_index('First Name')
df.set_index('First Name', inplace=True)

df.sort_index(inplace=True)

# loc used with index values, should be preferred way to index things
df.loc[...]

# iloc - numerical numpy-like indexing
df.iloc[...]

# works on Series as well

import random

first_names = df['First Name']

df['fullname'] = df['First Name'] + ' ' + df['Surname']
df['age'] = [random.randrange(20, 31) for _ in range(df.shape[0])]

age = df['age']
age + 2

first_names.str  # access string methods

df.drop(columns = df.columns[-2], inplace=True)
del df['column name']

col_name = df.columns[8]
# col.apply()  apply any function elementwise to column

expect = df[col_name]
expect.apply(lambda s: 'basic' in s)

age.to_numpy()
age.to_list()

# logical indexing
df['age'] > 25

df.loc[df['age'] > 25]
# bit operators &, |

# for missing values
np.NaN


isna()
notna()
fillna()
dropna()

# is the same as null versions
# R has NA and NULL

# SQL
'''
SELECT * from df
'''

# pandas 
df
'''
SELECT * from df
WHERE column = value
'''

df.loc[df['column'] == value]

...
# https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html

df.rename(columns={col_name: 'expect'}, inplace=True)

df.columns = [col.lower() for col in df]



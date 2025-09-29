import pandas as py
import os

 

df = py.read_json(r"E:\PYTHON-main\pandas\sample_Data.json")

print("represent first 4 data from beginning = ")
print(df.head(4))
print("represent first 4 data from end = ")
print(df.tail(4))


print(df.info())
print(df.describe())

# why is it important
# Finance / Stock Market

# df.head() → see first trading days.

# df.tail() → see last trading days to analyze recent performance.

"""
shapes - provides detail about how much rows and column are in dataset
column - display columns
"""

print(df.shape)
print(df.columns )
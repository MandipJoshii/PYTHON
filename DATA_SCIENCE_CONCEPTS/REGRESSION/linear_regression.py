#without scikit learn


#we need:
#1. x,y
#2. table representing x,y,xy,x2
#3. formulas:
#y = b0 + b1x + e
# b1 = x-x_mean-y-y_mean/(x-x_mean)**2
#b0 = y_mean - b1*x_mean


"""
remember to put the x and y value in df(dataframe) for data cleaning and visualization

NOTE:

X represent X data from table which is 1,2,3,4,5
Y represents Y data from table which is 6,7,8,9,10

X_mean = 1+2+3+4+5/5
y_mean = 6+7+8+9+10/5

SO:
numerator = x-x_mean - y-y_mean
denomiantor = (x-x_mean)**2

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as py

table = {
    "X":[1,2,3,4,5],
    "Y":[6,7,8,9,10]
}

# print(table)
df = py.DataFrame(table)

x_mean = np.mean(df["X"])
y_mean = np.mean(df["Y"])

# print(x_mean)
# print(y_mean)
df.to_excel("linear_regression.xlsx",index=False)

numerator = np.sum(df["X"]-x_mean*df["Y"]-y_mean)
denominator = np.sum((df["X"]-x_mean)**2)
print(numerator)
print(denominator)
b1 = numerator/denominator

print(f"Slope: {b1}")


b0 = np.sum(y_mean-b1*x_mean)
print(f"Intercept: {b0}")

df["y_value"] = b0+b1*df["X"]

print(df["y_value"])



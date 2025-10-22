from sklearn.datasets import fetch_california_housing #a bunch object -> means load dataset into memory
import pandas as pd
content = fetch_california_housing()

# print(data)
print("<--------------------------------DATA TYPE------------------------------------------->")
print(type(content))
#print(content.data) shows the data of content variable
print("<--------------------------------DATA FRAMING------------------------------------------->")

df = pd.DataFrame(content.data,columns=content.feature_names) #represents total number of column in california_housing
print(df)
print("<--------------------------------TARGET------------------------------------------->")

print(content.target)
print("<--------------------------------DESCR------------------------------------------->")

print(content.DESCR)
print("<--------------------------------SHAPE------------------------------------------->")

print(content.data.shape)
print("<--------------------------------SIZE------------------------------------------->")

print(content.data.size)
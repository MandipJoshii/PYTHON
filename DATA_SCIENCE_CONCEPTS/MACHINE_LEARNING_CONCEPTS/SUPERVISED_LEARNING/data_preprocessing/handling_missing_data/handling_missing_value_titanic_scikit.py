import pandas as pd
from sklearn.impute import SimpleImputer 

titanic = pd.read_csv("Titanic-Dataset.csv")


print(titanic.shape)

#imputing numerical data from titanic
num_imputer = SimpleImputer(strategy='mean')

titanic[['Age']] = num_imputer.fit_transform(titanic[['Age']])
print(titanic[['Age']])


cat_imputer = SimpleImputer(strategy='most_frequent')

titanic[['Cabin']] = cat_imputer.fit_transform(titanic[['Cabin']])

print(titanic[['Cabin']])


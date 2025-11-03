import pandas as pd
from sklearn.impute import SimpleImputer
titanic = pd.read_csv("Titanic-dataset.csv")
# print(titanic.head(5))

# print(titanic.dropna())

# titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())

# print(titanic["Age"])

# titanic["Cabin"] = titanic["Cabin"].fillna(titanic["Cabin"].mode())
# print(titanic["Cabin"])

num_impute = SimpleImputer(strategy="mean") # or median

titanic[["Age"]] = num_impute.fit_transform(titanic[["Age"]])

print(titanic[["Age"]])


cat_impute = SimpleImputer(strategy="most_frequent")

titanic[["Cabin"]] = cat_impute.fit_transform(titanic[["Cabin"]])

print(titanic["Cabin"])
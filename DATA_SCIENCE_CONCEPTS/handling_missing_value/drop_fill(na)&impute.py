import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
titanic = pd.read_csv("Titanic-dataset.csv")
# print(titanic.head(5))

# print(titanic.dropna())

# titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())

# print(titanic["Age"])

# titanic["Cabin"] = titanic["Cabin"].fillna(titanic["Cabin"].mode())
# print(titanic["Cabin"])


num_column = ["Age", "Fare"]
cat_column = ["Cabin", "Embarked"]


num_impute = SimpleImputer(strategy="mean") # or median

titanic[["Age"]] = num_impute.fit_transform(titanic[["Age"]])

print(titanic[["Age"]])


cat_impute = SimpleImputer(strategy="most_frequent")

titanic[["Cabin"]] = cat_impute.fit_transform(titanic[["Cabin"]])

print(titanic["Cabin"])

preprocessor = ColumnTransformer([
   ("num", num_impute,num_column),
   ("cat",cat_impute,cat_column)
])

titanic_transformed = preprocessor.fit_transform(titanic)

titanic_transformed_df = pd.DataFrame(
    titanic_transformed,columns=num_column+cat_column
)

print(titanic_transformed_df.head(5))
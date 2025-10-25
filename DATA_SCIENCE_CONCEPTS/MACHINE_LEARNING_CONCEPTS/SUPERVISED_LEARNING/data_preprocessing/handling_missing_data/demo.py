import pandas as pd

titanic = pd.read_csv("Titanic-Dataset.csv")

print(titanic.shape)
print(titanic.size)

# print(titanic.isnull())

#removing the rows and columns of missing value
print(titanic.dropna())
print(titanic.dropna().size)

#this code will not work till you comment the code -> for larger missing value (>=30%)one
# titanic['Age'] = titanic['Age'].fillna(titanic['Age'].mean())
# print(titanic['Age'])

# titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())
# print(titanic['Age'])



titanic['Cabin'] = titanic['Cabin'].fillna(titanic['Cabin'].mode()[0])
print(titanic['Cabin'])


#for larger missing value(>=30%)

missing_percentage = titanic['Age'].isnull().mean()*100
print(missing_percentage) 


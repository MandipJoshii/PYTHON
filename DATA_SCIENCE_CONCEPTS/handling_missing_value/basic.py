from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer #handling missing value
from sklearn.preprocessing import StandardScaler, OneHotEncoder,MinMaxScaler #feature scaling and preprocessing
from sklearn.model_selection import train_test_split #splitting and evaluation
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
import pandas as pd

titanic = pd.read_csv("Titanic-Dataset.csv")
x_train,y_train,x_test,y_test = 
num_tansformer = Pipeline([
    ("imputer",SimpleImputer(strategy="mean")),
    ("scaler",StandardScaler())
])

cat_transformer = Pipeline([
    ("imputer",SimpleImputer(strategy="most_frequent")),
    ("encoder",OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num",num_tansformer),
    ("cat",cat_transformer)
])

model = Pipeline([

("preprocessor",preprocessor),
("regression",LogisticRegression)
])

model_fit(x)
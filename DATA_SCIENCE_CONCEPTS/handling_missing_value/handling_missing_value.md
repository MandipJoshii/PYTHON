# 🧹 Handling Missing Data in Python Datasets

Missing data is common in datasets (`NaN`, empty rows, empty columns).  
Proper handling is **essential** before applying any Machine Learning model.

---

## ⚡ Basic Approaches

### 1️⃣ `dropna()` & `fillna()`
- **`dropna()`** → Removes rows or columns containing missing values
- **`fillna()`** → Replaces missing values with a statistic (mean, median, mode, most frequent)

**Example using Titanic dataset:**
```python
import pandas as pd

# Load dataset
titanic = pd.read_csv("Titanic-dataset.csv")

# Drop rows with any missing value
# print(titanic.dropna())

# Fill missing numerical values with mean
# titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())

# Fill missing categorical values with mode
# titanic["Cabin"] = titanic["Cabin"].fillna(titanic["Cabin"].mode())
from sklearn.impute import SimpleImputer

# Numerical Imputer for 'Age' column
num_impute = SimpleImputer(strategy="mean")  # or "median"
titanic[["Age"]] = num_impute.fit_transform(titanic[["Age"]])
print(titanic[["Age"]])

# Categorical Imputer for 'Cabin' column
cat_impute = SimpleImputer(strategy="most_frequent")
titanic[["Cabin"]] = cat_impute.fit_transform(titanic[["Cabin"]])
print(titanic["Cabin"])


Why use SimpleImputer instead of fillna() / dropna()?

Dynamic: Learns from data and can apply to new datasets

Reusable: fit_transform() allows consistent application across datasets

Automated: Handles missing values without manually specifying mean, median, or mode

Consistent: Ensures same preprocessing logic every time

fillna() and dropna() are static — cannot adapt to new or similar datasets.
SimpleImputer is ML-friendly, essential for pipelines.
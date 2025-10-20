import matplotlib.pyplot as plt
import pandas as py
import seaborn as sb

titanic = py.read_csv("Titanic-Dataset.csv")

df = py.DataFrame(titanic)

print(df.head(5))

sb.countplot(x='Survived',data=df)
plt.title("TITANIC SURVIVED AND DEAD PEOPLE COUNT")
plt.xlabel("SURVIVED(0=NO,1=YES)")
plt.ylabel("PASSANGER")
plt.show()
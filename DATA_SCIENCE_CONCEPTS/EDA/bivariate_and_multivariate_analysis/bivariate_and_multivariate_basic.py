import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

titanic = pd.read_csv("Titanic-Dataset.csv")
flights = pd.read_csv("flights.csv")
resturants = pd.read_csv("resturant.csv")
deliveries = pd.read_csv("deliveries.csv")
laptop = pd.read_csv("laptop_purchase.csv")
tips = pd.read_csv("tip.csv")
# print(tips.head(5))


#display using seaborn

# sb.countplot(x='minute',data=flights)
# plt.title("TIMES IN MINUTES")

#1. scatterplot (numerical,numerical)

#bivariate anlysis
# sb.scatterplot(x='total_bill',y='tip',data=tips,hue=tips['sex'])
# plt.show()

#multivariate analysis
# sb.scatterplot(x='total_bill',y='tip',data=tips,hue=tips['sex'],size=tips['smoker'])



#2. bar plot(numerical,categorical)


# sb.barplot(x='Pclass',y='Age',data=titanic,hue=titanic['size'])


#3. box plot(numerical,categorical)

# sb.boxplot(x='Sex',y='Age',data=titanic,hue=titanic['Survived'])


#4. Dist plot(numerical,categorical)
# sb.displot(x='Age', data=titanic, hue='Survived', multiple='stack', kind='kde')
# plt.title("Age Distribution by Survival Status")



#5. Heat Map(categorical,categorical)

sb.heatmap(data=titanic)
plt.show()
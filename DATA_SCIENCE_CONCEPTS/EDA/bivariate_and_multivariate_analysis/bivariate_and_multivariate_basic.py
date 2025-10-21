import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


flights = pd.read_csv("flights.csv")
resturants = pd.read_csv("resturant.csv")
deliveries = pd.read_csv("deliveries.csv")
laptop = pd.read_csv("laptop_purchase.csv")
tips = pd.read_csv("tip.csv")
print(tips.head(5))


#display using seaborn

# sb.countplot(x='minute',data=flights)
# plt.title("TIMES IN MINUTES")


#bivariate anlysis
# sb.scatterplot(x='total_bill',y='tip',data=tips,hue=tips['sex'])
# plt.show()

#multivariate analysis
sb.scatterplot(x='total_bill',y='tip',data=tips,hue=tips['sex'],size=tips['smoker'])
plt.show()
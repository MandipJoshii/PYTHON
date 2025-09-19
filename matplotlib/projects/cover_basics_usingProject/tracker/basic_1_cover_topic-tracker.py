# Weekly Personal Activity & Expense Tracker
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
# kitchen_inventories as kitchen_inv
#for expenses tracker
kitchen_inv = ['fruits','wok','chicken','dish cleaner','knife set']

expenses_cost = np.random.randint(200,1500,size=(5))

#just checking the value
print(expenses_cost)
print(kitchen_inv)

#tea_consupmtion_traceker as tct
# tct = np.random.randint(1,4,7) or ↓	

tct = np.random.randint(1,4,size=(7))
print(tct)

fig, axs = plt.subplots(2, 3, figsize=(50, 30))  # 2 rows, 3 columns
fig.suptitle("Weekly Personal Activity & Expenses Tracker", fontsize=16)


#for plot()
axs[0,0].plot(kitchen_inv,expenses_cost,color="green",linestyle="--",linewidth="3",marker="o",label="expenses")
axs[0,0].set_xlabel("Kitchen Inv")
axs[0,0].set_ylabel("Cost of Goods")
axs[0,0].legend()
axs[0,0].grid(color="purple",linestyle=":")
plt.show()

#tomorrow pie,scatter,bar,horizontal, histogram and tight_layer concept
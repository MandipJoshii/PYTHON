# Weekly Personal Activity & Expense Tracker
import matplotlib.pyplot as plt
import numpy as np


x = [1,3,2,7,9]
y = [2,4,7,8,11]

plt.plot(x,y, color="green", linestyle="--",linewidth="3",marker="o",label="numbers")
plt.legend()
plt.grid(color="yellow", linestyle="-", linewidth="2")
plt.title("random")
plt.xlabel("x value")
plt.ylabel("y value")
# plt.xlim(1,8)
# plt.ylim(2,9)
plt.show()
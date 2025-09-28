import numpy as np
import matplotlib.pyplot as plt


name = np.array(["x","y","z","a","b","c"])
marks = np.array([90,80,70,60,50,49])

plt.bar(name,marks)
plt.title("STUDENT MARKS")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.show()  

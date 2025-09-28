import numpy as np

np.random.seed(0)
# value in seed is determine using a specific formula
#which is:
#formula:
#number = int(f1 * (high - low) + low)
#where f1...fn is defined by numpy
#NOTE: F1 TO FN COULD BE CALCULATED BUT I HAVENT STUDIED DETAILY
#from np.random.randint(1,10) -> high is 10 and low is 1
# SO:
#number = (f1 * (10-1) + 1) = 6


print(np.random.randint(1,10))


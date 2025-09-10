import numpy as np

#data

marks = np.array([10,12,14,16,18,20])


# 1. lets use SUM to find TOTAL
print("<-----------------------SUM---------------------------------->")
total = np.sum(marks)
print(total)

# 2. lets use PRODUCT to find MULTIPLICATION OF SEQUENTIAL NUMBER
print("<----------------------PRODUCT----------------------------------->")
prod = np.prod(marks)
print(prod) # OUTPUT => 10*12*14*16*18*20 = 9676800

# 3. lets use mean, median to find AVERAGE,
print("<-------------------------MEAN,MEDIAN,AVERAGE,VARIANCE,STANDARD DEVIATION-------------------------------->")

mean = np.mean(marks)
average = np.average(marks)
median = np.median(marks)
var = np.var(marks)
sd = np.std(marks)

print(mean)
print(average)
print(median)
print(var)
print(sd)


# 4. mini,max
print("<-------------------------MINI,MAX,ARGMINI,ARGMAX-------------------------------->")

mini = np.min(marks)
max = np.max(marks)
argmini = np.argmin(marks)
argmax = np.argmax(marks)

print(mini)
print(argmini)
print(max)
print(argmax)

print("<--------------------------------------------------------->")


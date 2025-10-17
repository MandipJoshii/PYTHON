#this is a very very simple example to represent eda later titanic dataset will be used to learn same concept deeply and in more understandable way


import matplotlib.pyplot as plt
import pandas as py

data ={
    "iq":[10,20,30,40,50,60],
    "cgpa":[1,1.5,2,2.5,3,3.5]
}

df = py.DataFrame(data)
df.to_csv("job.csv",index=False)
print(df)

#how big is the data
print("\n",df.shape) #data is of 6,2

#how does the data looks
print("\n",df.sample(6))

#data type in col
print("\n",df.info())

#missing value(null value)
print("\n",df.isnull().sum())

#duplicated value
print("\n",df.duplicated().sum())

#correlation
print(df.corr())

#maths
print(df.describe())

plt.scatter(x="iq",y="cgpa",data=df)
plt.title("JOB")
plt.show()
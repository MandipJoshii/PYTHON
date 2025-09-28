import pandas as py
import os
data = {
    "name":["x","y","z"],
    "place":["a","b","c"],
    "age":[20,40,50]
}
 

df = py.DataFrame(data)

print(df)


df.to_csv("result.csv", index=False)
df.to_excel("result.xlsx",index=False) #this work after downloading openpyxl    


print("File saved at : ", os.getcwd())
import json

try:
 with open("json_demo.txt","r") as file:
    content = file.read().strip()
    if content:
        tasks = json.loads(file)

    else: raise FileNotFoundError 
except FileNotFoundError:
   
   print(2+2)

# main code


with open("json_demo.txt","w") as file:
   json.dumps(file,tasks,indent=4)



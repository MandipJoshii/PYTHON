import json


data = [
    {"name":"mandip","age":21,"hobbies":"x,y,z","student":True}
]


json_converting = json.dumps(data,indent=4)
print(json_converting)

back_to_python = json.loads(json_converting)
print(back_to_python)


print(type(back_to_python))
print(back_to_python[0]["name"])
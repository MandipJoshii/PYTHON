item = ["banana","spatula","wok","oven","ventilation"]

find = "wok"

for i, items in enumerate(item, start = 1):
    if items == find:
        
        print(f"found = {find}")
        print(f"at index = {i}")
        break
    else:
        print("no item found")    
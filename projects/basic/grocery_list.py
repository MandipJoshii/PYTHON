grocery = []

grocery.append("mango")
grocery.insert(1,"eggs")
grocery.extend(["brush"])
print(grocery)

#////////////////////////////////////////////////////////


todo_task = ["clean","cook","bath","study"]

# todo_task.pop(1)
# todo_task.pop(0)
# todo_task.pop(1)
# todo_task.pop(0)
while todo_task != []:
    completed_task = todo_task.pop(0)
    
    print(f"COMPLETED TASK = {completed_task}")
    
    print(f"REMAINING TASK = {todo_task}")
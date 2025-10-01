


#status = completed(c), pending(p), skip(s)

#features = add(a)/remove(r)
tasks = [
    {"name":"cleaning_room","status":"pending"},
    {"name":"cooking","status":"pending"},
    {"name":"shopping","status":"pending"},
    {"name":"spa","status":"pending"},
    {"name":"throw_garbage","status":"pending"}
]

while True:
    print("WELCOME TO YOURS TO-DO LIST")

    for i,task in enumerate(tasks):
        print(task["name"] , "-", task["status"])
    option = input("CHOOSE OPTION: (ADD|REMOVE|COMPLETE|QUIT): ")

    if option == "add":
        name = input("ENTER TASK YOU WANT TO ADD: ")
        tasks.append({"name":name, "status":"pending"})

    elif option == "remove":
        num=int(input("ENTER THE NUMBER OF THE TASK YOU WANT TO REMOVE: "))
        tasks.pop(num)

    elif option == "complete":
     num = int(input("ENTER THE NUMBER OF WHICH TASK HAVE YOU COMPLETED: "))
     tasks[num]["status"] = "completed"


    elif option == "quit":
     break
     

# file 


# file = open("todo-list.txt","a")


# file.write(str(tasks) + "\n" + "\n")


# file.close()
"""
this was a failure because:
Append mode only writes to the file. Python never loads the file back into memory.
So every time we restart, Python ignores what was saved and uses the original tasks list.
IT COULD BE SOLVED PUT THE PROGRAM WOULD BE COMPLEX AND NOT READABLE


BEST WAY IS TO USE JSON
"""



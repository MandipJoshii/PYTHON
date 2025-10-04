import json


try:
    with open("contact_book.json","r") as file:
        content = file.read().strip()

        if content:
           contact = json.loads(content)
        else:
            raise FileNotFoundError
except FileNotFoundError:
    contact = []

while True:
    print("\n WELCOME TO YOUR CONTACT BOOK \n")

    if not contact:
       print("\n ADD A CONTACT TO YOUR LIST \n")
    else:
       for i,c in enumerate(contact):
        print(f"{i}.{c['name']} - {c['age']} - {c['contact_number']} - {c['email']}")   
        print("\n OPTIONS: ADD|VIEW|SEARCH|UPDATE|DELETE|QUIT")     
    

    choice = input("ENTER YOUR CHOICE: ").lower()

    if choice == 'add':
        name = input("ENTER THE NAME OF THE PERSON YOU WANT TO ADD: ")
        age = input("WHAT'S YOUR AGE, INPUT HERE: ")
        contact_number = input("ENTER YOUR CONTACT NUMBER: ")
        email = input("ENTER YOUR EMAIL: ")
        contact.append({"name":name, "age":age,"contact_number":contact_number,"email":email})


    elif choice == "quit":
     break  


with open("contact_book.json", "w") as file:
       json.dump(contact,file,indent=4)

print("\n CONTACT SAVED SUCCESSFULLY  \n")           



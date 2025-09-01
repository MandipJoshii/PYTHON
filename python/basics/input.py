age = int(input("ENTER YOUR AGE : "))

access = True

if age >=18 and access:
    print("YOU ARE ALLOWED TO ENTER IN THE CLUB")
elif age < 18 and age >= 15:  
    if access:
     print("YOU ARE ALLOWED TO ENTER BECAUSE USER HAS A ACCESS PASS") 
    else:
        print("SORRY YOU ARE NOT ALLOWED TO ENTER IN THE CLUB(NEED ACCESS PASS)")
else:
    print("SORRY YOU ARE NOT ALLOWED TO ENTER IN THE CLUB")

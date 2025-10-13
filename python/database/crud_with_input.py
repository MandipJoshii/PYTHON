import sqlite3 as sq

conn = sq.connect("input.db")


cursor = conn.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS STUDENTS(
               id INTEGER PRIMARY KEY,
               name VARCHAR(30),
               age int
               )""")

cursor.execute("DELETE FROM STUDENTS")



while True:

 print("WELCOME TO YOUR DATABASE: ")


 id = int(input("ENTER YOUR ID: "))
 name = input("ENTER YOUR NAME: ")
 age = int(input("ENTER YOUR AGE: "))
 cursor.execute("INSERT INTO STUDENTS(id,name,age) VALUES(?,?,?)",(id,name,age))
 conn.commit()

 ask = input("DO YOU ADD MORE TO YOUR DATABASE: (YES/NO)").lower()

 if ask != "yes":
  break



conn.close()






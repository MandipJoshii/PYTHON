import sqlite3 as sq

conn = sq.connect("create.db")
print("\n CONNECTION MADE SUCCESSFULLY \n")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS STUDENTS(
               id int,
               name VHARCHAR(50),
               age int
               )
""")
print("\n TABLE CREATED SUCCESSFULLY \n")



cursor.execute("INSERT INTO STUDENTS(id,name,age) VALUES (?,?,?)",(101,"josh",21))
cursor.execute("INSERT INTO STUDENTS(id,name,age) VALUES (?,?,?)",(102,"hazel",22))




conn.commit()



conn.close()
print("\n DATA INSERTED SUCCESSFULLY \n")

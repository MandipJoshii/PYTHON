import sqlite3 as sq


conn = sq.connect("delete_demo.db")


cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS STUDENTS(
               id INTEGER PRIMARY KEY,
               name VHARCHAR(100),
               age INT
               )
""")

cursor.execute("DELETE FROM STUDENTS")

cursor.execute("INSERT INTO STUDENTS(id,name,age) VALUES (?,?,?)", (101,"leomord",20))
cursor.execute("INSERT INTO STUDENTS(id,name,age) VALUES (?,?,?)", (102,"messi",22))
cursor.execute("INSERT INTO STUDENTS(id,name,age) VALUES (?,?,?)", (103,"alucard",23))

cursor.execute("UPDATE STUDENTS SET name=?,age=? WHERE id=?",("travis",21,101))
cursor.execute("UPDATE STUDENTS SET name=?,age=? WHERE id=?",("cummin",22,102))
cursor.execute("UPDATE STUDENTS SET name=?,age=? WHERE id=?",("marsh",22,103))

cursor.execute("UPDATE STUDENTS SET name=?,age=? WHERE id=?",("travis",21,101))

cursor.execute("DELETE FROM STUDENTS WHERE id = ?",(101,))
print("\n DELETED SUCCESSFULLY \n")


cursor.execute("SELECT * FROM STUDENTS")
record = cursor.fetchall()

print("\n TABLE DATA UPDATED \n")

for r in record:
    print(f"ID: {r[0]} - NAME: {r[1]} - AGE: {r[2]}")


conn.commit()
conn.close()
import sqlite3 as sq
# import module.anywhere_use as db

# db.database()
conn = sq.connect("database.db")


cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS STUDENTS(
               id int,
               name VHARCHAR(50),
               age int
               )
"""
    )


cursor.execute("INSERT INTO STUDENTS(id,name,age) VALUES (?,?,?)",(101,"mandip",21))
cursor.execute("INSERT INTO STUDENTS(id,name,age) VALUES (?,?,?)",(102,"josh",21))
cursor.execute("INSERT INTO STUDENTS(id,name,age) VALUES (?,?,?)",(103,"hazelwood",22))

cursor.execute("SELECT * FROM STUDENTS")

record = cursor.fetchall()

print("\n STUDENT RESULT \n")

for r in record:
    print(f"ID: {r[0]} - NAME: {r[1]} - AGE: {r[2]}")


conn.commit()
conn.close()





#if want to reduce code and make it look more cleaner 



# import sqlite3 as sq
# import module.anywhere_use as db

# db.database()
# conn = sq.connect("database.db")


# cursor = conn.cursor()

# cursor.execute("SELECT * FROM STUDENTS")

# record = cursor.fetchall()

# print("\n STUDENT RESULT \n")

# for r in record:
#     print(f"ID: {r[0]} - NAME: {r[1]} - AGE: {r[2]}")


    
# conn.close()




import sqlite3 as sq

def database():
    connection = sq.connect("database.db")

    cursor = connection.cursor()

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


    connection.commit()

    connection.close()
    print("\n DATA INSERTED SUCCESSFULLY \n")

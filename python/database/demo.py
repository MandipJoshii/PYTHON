import sqlite3 as sq

connection = sq.connect("demo.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS STUDENT(
               id int,
               name VARCHAR(50),
               roll_no int             
    )
""")


connection.commit()

connection.close()
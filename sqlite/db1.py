
import os
import sqlite3

conn = sqlite3.connect("userboxes.db")
cursor = conn.cursor()

def insertuser():
    table='users1'
    #id=1267
    user='yurasoft1972'
    cursor.execute("""insert into users1(user) values ('yurasoft1972123')""")
    conn.commit()  
    
def delete(table: str, row_id: int) -> None:
    row_id = int(row_id)
    cursor.execute(f"delete from {table} where id={row_id}")
    conn.commit()



insertuser()
#insert into users(id,user) values ('124','123');


#"""INSERT INTO sqlitedb_developers(id, name, email, joining_date, salary) VALUES (4, 'Alex', 'sale@gmail.com', '2020-11-20', 8600);"""
#"""INSERT INTO sqlitedb_developers(id, name, email, joining_date, salary) VALUES (4, 'Alex', 'sale@gmail.com', '2020-11-20', 8600);"""


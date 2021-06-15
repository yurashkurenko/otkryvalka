import os
from typing import Dict, List, Tuple

import sqlite3


conn = sqlite3.connect("boxusers.db")
cursor = conn.cursor()


def insert(table: str, column_values: Dict):
    columns = ', '.join( column_values.keys() )
    values = [tuple(column_values.values())]
    placeholders = ", ".join( "?" * len(column_values.keys()) )
    cursor.executemany(
        f"INSERT INTO {table} "
        f"({columns}) "
        f"VALUES ({placeholders})",
        values)
    conn.commit()


def fetchall(table: str, columns: List[str]) -> List[Tuple]:
    columns_joined = ", ".join(columns)
    cursor.execute(f"SELECT {columns_joined} FROM {table}")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        dict_row = {}
        for index, column in enumerate(columns):
            dict_row[column] = row[index]
        result.append(dict_row)
    return result
    
def fetchidforusers(user: str) -> List[id]:
#cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
    cursor.execute(f"SELECT id FROM 'users' WHERE user='{user}'")
    id = cursor.fetchall()
    todelete=[]
    for i in range(len(id)):
        todelete.append(id[i][0])
    return todelete
    
def fetchidforboxes(box: str) -> List[id]:
#cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
    cursor.execute(f"SELECT id FROM 'boxes' WHERE box='{box}'")
    id = cursor.fetchall()
    todelete=[]
    for i in range(len(id)):
        todelete.append(id[i][0])
    return todelete

def getlistuserforbox(box:str)  -> str:
    cursor.execute(f"select users FROM boxes WHERE box='{box}'")
    result = cursor.fetchone()
    conn.commit()
    users=''
    if not (result is None):
        users = result[0]
    print(users)
    return users

def setlistuserforbox(box:str,users:str)  -> None:
    cursor.execute(f"update boxes set users = '{users}' where box = '{box}'")
   # UPDATE boxes set users='123' where box='box1'
    result = cursor.fetchall()
    conn.commit()
    return
    
def setlistuserforbox1(box:str,users:str)  -> None:
    cursor.execute(f"update boxes set users = '{users}' where box = '{box}'")
   # UPDATE boxes set users='123' where box='box1'
    result = cursor.fetchall()
    return    
#     sqlline=f"update menulevel set ml = '{menulevelstr}' where id = 1"   

def fetchcelltext(table: str, column: str, row: int) -> str:
    cursor.execute(f"SELECT {column} FROM {table} where id={row}")
    result = cursor.fetchone()
    return result

def delete(table: str, row_id: int) -> None:
    row_id = int(row_id)
    cursor.execute(f"delete from {table} where id={row_id}")
    conn.commit()


def get_cursor():
    return cursor


def _init_db():
    """Инициализирует БД"""
    with open("createdb.sql", "r") as f:
        sql = f.read()
    cursor.executescript(sql)
    conn.commit()


def check_db_exists():
    """Проверяет, инициализирована ли БД, если нет — инициализирует"""
    cursor.execute("SELECT name FROM sqlite_master "
                   "WHERE type='table' AND name='expense'")
    table_exists = cursor.fetchall()
    if table_exists:
        return
    _init_db()

def updateml(menulevelstr: str) -> None:
#    print(menulevelstr)
    sqlline=f"update menulevel set ml = '{menulevelstr}' where id = 1"
#    print(sqlline)
    cursor.execute(sqlline)
    conn.commit()

def updatemsb(messagestr: str) -> None:
    sqlline=f"update messagestringbuffer set message = '{messagestr}' where id = 1"
    cursor.execute(sqlline)
    conn.commit()

def updateselectedbox(box: str) -> None:
    sqlline=f"update 'selectedboxusers' set 'box' = '{box}'"
    cursor.execute(sqlline)
    conn.commit()
    
def updateselecteduser(user: str) -> None:
    sqlline=f"update selectedboxusers set user = '{user}'"
    cursor.execute(sqlline)
    conn.commit()

check_db_exists()



#"""Update sqlitedb_developers set salary = 10000 where id = 4"""
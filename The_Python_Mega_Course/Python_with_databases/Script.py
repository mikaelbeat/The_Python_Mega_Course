import sqlite3
import os.path
from os import path

database = "database.db"


def check_database():
    if path.exists(database):
        print(f"Database {database} already found!\n")
    else:
        print(f"Created database {database}.\n")
        

def create_table():
    check_database()
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()
    
        
def insert_to_table(item, quantity, price):
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()
    print(f"Inserted to {database} new item {item}, quantity {quantity}, price {price}.\n")
    
    
def view_database():
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    items = cur.fetchall()
    conn.close()
    return items


def delete_item(item):
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = ?", (item,))
    conn.commit()
    conn.close()
    
    
def update_item(quantity, price, item):
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = ?, price = ? WHERE item = ?", (quantity, price, item))
    conn.commit()
    conn.close()
    
    
    
create_table()
#insert_to_table("Wine Glass", 20, 7.5)
print(view_database())
#delete_item("Wine Glass")
print(view_database())
update_item(60, 2.3, "Coffee cup")
print(view_database())
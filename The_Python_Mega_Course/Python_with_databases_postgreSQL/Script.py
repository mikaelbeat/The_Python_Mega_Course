import psycopg2


database = "dbname='test_database' user='postgres' password='admin' host='localhost' port='5432'"


def create_table():
    conn = psycopg2.connect(database)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()
    
        
def insert_to_table(item, quantity, price):
    conn = psycopg2.connect(database)
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()
    print(f"Inserted to database new item {item}, quantity {quantity}, price {price}.\n")
    
    
def view_database():
    conn = psycopg2.connect(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    items = cur.fetchall()
    conn.close()
    return items


def delete_item(item):
    conn = psycopg2.connect(database)
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = %s", (item,))
    print(f"Deleted {item} from database.")
    conn.commit()
    conn.close()
    
    
def update_item(quantity, price, item):
    conn = psycopg2.connect(database)
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s", (quantity, price, item))
    conn.commit()
    conn.close()
    
    
    
create_table()
#insert_to_table("Karambola", 50, 4.5)
print(view_database())
#delete_item("Wine Glass")
print(view_database())
update_item(40, 2.3, "Karambola")
print(view_database())










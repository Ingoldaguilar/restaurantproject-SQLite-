# imports
import sqlite3

# functions

# create db
def create_db():
    # create connection
    connection = sqlite3.connect("restaurant.db")
    # create cursor
    cursor = connection.cursor()

    try:
        cursor.execute("""
        CREATE TABLE category(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name VARCHAR(100) UNIQUE NOT NULL
        ) 
        """)
    except sqlite3.OperationalError:
        print("The table 'category' already exist.")
    else:
        print("Table 'category' created successfully.")

    try:
        cursor.execute("""
        CREATE TABLE dish(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name VARCHAR(100) UNIQUE NOT NULL, 
                category_id INTEGER NOT NULL, 
                FOREIGN KEY(category_id) REFERENCES category(id)
        ) 
        """)
    except sqlite3.OperationalError:
        print("The table 'dish' already exist.")
    else:
        print("Table 'dish' created successfully.")

    # close the connection
    connection.close()

create_db()
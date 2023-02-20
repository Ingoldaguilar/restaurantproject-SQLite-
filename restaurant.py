# imports
import sqlite3

# functions

# create db
def create_db():
    # create connection
    connection = sqlite3.connect("restaurant.db")
    # create cursor
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE category(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name VARCHAR(100) UNIQUE NOT NULL
    ) 
    """)

    cursor.execute("""
    CREATE TABLE dish(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name VARCHAR(100) UNIQUE NOT NULL, 
            category_id INTEGER NOT NULL, 
            FOREIGN KEY(category_id) REFERENCES category(id)
    ) 
    """)

    # close the connection
    connection.close()

create_db()
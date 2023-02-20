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

# add category
def add_category():
    category = input("Name of the new category\n>")

    connection = sqlite3.connect("restaurant.db")
    cursor = connection.cursor()

    try:
        # insert the new category
        cursor.execute(f"INSERT INTO category VALUES(null, '{category}') ")
    except sqlite3.IntegrityError:
        print(f"Error: The category '{category}' already exist.")
    else:
        print(f"Category '{category}' created successfully.")

    # save and close
    connection.commit()
    connection.close()

# add dish
def add_dish():
    connection = sqlite3.connect("restaurant.db")
    cursor = connection.cursor()

    # show categories to the user
    categories = cursor.execute("SELECT * FROM category").fetchall()

    print("Select a category for the dish:")
    for category in categories:
        print(f"[{category[0]}] {category[1]}") # id and name

    # get the category
    category_id = int( input(">") )

    # get the dish
    dish = input("Name of the new dish\n>")
    try:
        cursor.execute(f"INSERT INTO dish VALUES(null, '{dish}', {category_id}) ")
    except sqlite3.IntegrityError:
        print(f"Error: The dish '{dish}' already exist.")
    else:
        print(f"Dish '{dish}' created successfully.")

    # save and close
    connection.commit()
    connection.close()



# create db
create_db()

# show menu
while True:
    print("\nWelcome to the restaurant manager")
    option = input("\nInsert a option:\n[1] Add a category\n[2] Add a dish\n[3] Exit\n>")

    if option == "1":
        add_category()

    elif option == "2":
        add_dish()

    elif option == "3":
        print("Bye!")
        break

    else:
        print("Error: select a valid option")
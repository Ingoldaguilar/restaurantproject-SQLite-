# imports
import sqlite3
from tkinter import *

# create the root
root = Tk()
root.title("Flavors of the World - Menu")
root.resizable(False, False)
root.config(bd=25, relief="sunken")

# label
Label(root, text="   Flavors of the World   ", fg="darkgreen", font=("Times New Roman",28,"bold italic")).pack()
Label(root, text="Menu of the day", fg="green", font=("Times New Roman",24,"bold italic")).pack()
Label(root, text="").pack()  # break


# connect to the db
connection = sqlite3.connect("restaurant.db")
cursor = connection.cursor()

# get categories and dishes
categories = cursor.execute("SELECT * FROM category").fetchall()
for category in categories:
    Label(root, text=category[1], fg="black", font=("Times New Roman", 20, "bold italic")).pack()

    dishes = cursor.execute(f"SELECT * FROM dish WHERE category_id={category[0]}").fetchall()
    for dish in dishes:
        Label(root, text=dish[1], fg="gray", font=("Verdana", 15,  "italic")).pack()

    Label(root, text="").pack()  # break

# close connection
connection.close()

# show price
Label(root, text="12€ (IVA incl.)", fg="darkgreen", font=("Times New Roman", 20, "bold italic")).pack(side="right")

# mainloop
root.mainloop()
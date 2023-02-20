# imports
import sqlite3

# create connection
connection = sqlite3.connect(".db")
# create cursor
cursor = connection.cursor()





# commit changes
connection.commit()
# close
connection.close()
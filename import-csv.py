import csv
from init_db import db_connection
import random
from werkzeug.security import generate_password_hash


hash = generate_password_hash('cookzone')

cursor, connection = db_connection(r"./databases/database.db")
cursor.execute("""CREATE TABLE IF NOT EXISTS Menu (ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
                                ItemType TEXT,
                                Ingredients TEXT,
                                Description TEXT,
                                course TEXT,
                                flavour TEXT,
                                Price INTEGER);
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS customer (CustID INTEGER PRIMARY KEY AUTOINCREMENT,
						Name TEXT,
						Email TEXT,
						pwdhash TEXT,
						phone_number INTEGER);""")

connection.commit()

# with open('./datasets/indian_food.csv') as csvfile:
#     menu_items = csv.reader(csvfile, delimiter=',')
#     for item in menu_items:
#         if item[0] =='name':
#             continue
#         else:
#             cursor.execute("""INSERT INTO menu (ItemType, Ingredients, Description, course, flavour) VALUES (?, ?, ?, ?, ?);""", (item[0], item[1], item[2], item[6], item[5]))
#         connection.commit()

# # Inserting random prices in the database
# cursor.execute("""SELECT COUNT(ItemType) FROM menu """)
# count = cursor.fetchall()
# for i in range(count[0][0] + 1):
#     cursor.execute("""UPDATE menu SET Price=? WHERE ItemID=?;""", (random.randrange(10, 100), i))
#     connection.commit()
# cursor.close()
# connection.close()

with open('datasets/customers.csv') as csvfile:
    customers = csv.reader(csvfile, delimiter=',')
    for customer in customers:
        if customer[0] =='First Name':
            continue
        else:
            cursor.execute("""INSERT INTO customer (name, phone_number, Email, pwdhash) VALUES (?, ?, ?, ?);""", (customer[0] + " " + customer[1], customer[2], customer[0] + "." + customer[1] +  "@gmail.com", hash))
        connection.commit()
cursor.close()
connection.close()

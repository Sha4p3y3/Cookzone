from sqlite3 import connect

def db_connection(database):
    conn = connect(database)
    cur = conn.cursor()
    return cur, conn

#curr, con = db_connection('menu.db')
#curr.execute("""CREATE TABLE IF NOT EXISTS Menu (ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
#                                ItemType TEXT UNIQUE,
                                #Description TEXT,
                                #Price INTEGER);""")
#curr.execute("""INSERT INTO Menu(ItemType, Description, Price) VALUES ('Paneer Butter Masala', 'vegetarian', 123);""")
#curr.execute("""INSERT INTO Menu(ItemType, Description, Price) VALUES ('Chicken Butter Masala', 'non-vegetarian', 123);""")
#con.commit()
#curr.close()
#con.close()

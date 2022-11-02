CREATE TABLE IF NOT EXISTS order (OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
                                  OrderDate Date ....,
                                  OrderTime ,
                                  CustID
                                  StaffID);


CREATE TABLE IF NOT EXISTS Menu (ItemID INTEGER PRIMARY KEY AUTOINCREMENT
					   ItemType TEXT,
					   Description TEXT,
					   Price INTEGER);

CREATE TABLE IF NOT EXISTS customer (CustID INTEGER PRIMARY KEY AUTOINCREMENT,
						Name TEXT,
						phone_number INTEGER);

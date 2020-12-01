import sqlite3



class dbconnection(object):
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()

with dbconnection('shop.db') as conn:
    cursor = conn.cursor()
    cursor.execute(f"insert into Category (category_name) values ('test1')")

    a= cursor.execute(f"SELECT * from Category")
    print(a.fetchmany(10))
import sqlite3

connect = sqlite3.connect('cars.db')
cursor = connect.cursor()
# cursor.execute('insert into parking (price,model) values (1444,"Tesla")')
# connect.commit()

# id_ = input()

cursor.execute('SELECT * from parking')
for data in cursor.fetchmany(2):
    print(data)
cursor.close()

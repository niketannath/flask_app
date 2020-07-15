import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

qry = "CREATE TABLE if not exists users (id integer primary key, username text, password text)"
cursor.execute(qry)

qry = "CREATE TABLE if not exists items (id integer primary key, name text, price real)"
cursor.execute(qry)

#cursor.execute("INSERT INTO items VALUES ('nike',69.69)")

connection.commit()
connection.close()



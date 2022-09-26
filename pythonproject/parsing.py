
import sqlite3

conn = sqlite3.connect('orders.db')

cur = conn.cursor()


cur.execute("""SELECT *, users.fname, users.lname FROM orders
    LEFT JOIN users ON users.userid=orders.userid;""")


print(cur.fetchall())


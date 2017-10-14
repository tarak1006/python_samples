import _mysql
db=_mysql.connect(host="localhost",user="root",
                  passwd="kandula123")

db.query("""SELECT spam, eggs, sausage FROM breakfast
    WHERE price < 5""")

r=db.store_result()
# ...or...
r=db.use_result()

r.fetch_row()

\\\\\\\\\\\\\\\\\\\\\\\


import MySQLdb
db=MySQLdb.connect(passwd="moonpie",db="thangs")


c=db.cursor()
max_price=5
c.execute("""SELECT spam, eggs, sausage FROM breakfast
          WHERE price < %s""", (max_price,))


c.fetchone()
(3L, 2L, 0L)

c.executemany(
    """INSERT INTO breakfast (name, spam, eggs, sausage, price)
    VALUES (%s, %s, %s, %s, %s)""",
    [
        ("Spam and Sausage Lover's Plate", 5, 1, 8, 7.95),
        ("Not So Much Spam Plate", 3, 2, 0, 3.95),
        ("Don't Wany ANY SPAM! Plate", 0, 4, 3, 5.95)
    ])
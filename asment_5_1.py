
import MySQLdb
db=MySQLdb.connect(host="localhost",user="root",
                  passwd="kandula123")


c=db.cursor()
max_price=5
#c.execute("""SHOW DATABASES""""")
#for i in c.fetchall:
 #   print(i)
try:
    c.execute("CREATE DATABASE eswar")
except:
    c.execute("DROP DATABASE eswar")
    c.execute("CREATE DATABASE eswar")




c.execute("USE eswar")
c.execute("""SHOW TABLES""")
data=c.fetchone
print("%s"%data)



# Drop table if it already exist using execute() method.
#c.execute("DROP TABLE IF EXISTS EMPLOYEE")
'''
# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""

c.execute(sql)

db.close()
'''
'''c.execute("""SELECT spam, eggs, sausage FROM breakfast
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
    '''

sql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('%s', '%s', '%d', '%c', '%d' )" %('Mac', 'Mohan', 20, 'M', 2000)



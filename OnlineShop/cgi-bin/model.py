import pymysql

connection = pymysql.connect(host='localhost', port=3306, db='test', user='root', autocommit=True)
cursor = connection.cursor()

def addToCart(pid):
    query = "insert into cart values (%s)"
    cursor.execute(query, (pid))

def getProductsInCart():
    query = "select pid from cart"
    cursor.execute(query)
    return cursor.fetchall()

def signup(userid,email,password):
    query = "insert into users values(%s,%s,%s)"
    result = cursor.execute(query, (userid, email, password))
    return result

def login(email,password):
    query = "select * from users where email = %s and password = %s"
    result = cursor.execute(query, (email, password))
    if result == 1:
        data = cursor.fetchone()
        return data[0]
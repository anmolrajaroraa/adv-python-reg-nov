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
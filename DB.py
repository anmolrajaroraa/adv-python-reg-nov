import pymysql
connection = pymysql.connect(host='localhost', port=3306, db='test', user='root', autocommit=True)
cursor = connection.cursor()
# query = "select * from users"
name = 'mohan'
email = 'mohan2@gmail.com'
password = 'mohan1234'
# query = "insert into users values ('shyam', 'shyam@gmail.com', '1234')"
# query = f"insert into users values ('{name}', '{email}', '{password}')"
query = "insert into users values (%s,%s,%s)"
result = cursor.execute(query, (name, email, password))
# data = cursor.fetchall()
print(result)
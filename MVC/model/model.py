import pymysql
connection = pymysql.connect(host='localhost', port=3306, db='test', user='root', autocommit=True)
cursor = connection.cursor()

class User:

    userList = []

    def __init__( self , name , email , password ):
        self.name = name
        self.email = email
        self.password = password

    def __str__( self ):
        return str(self.__dict__)

# def register( name , email , password ):
#     userObject = User(name,email,password)
#     User.userList.append(userObject)
#     return User.userList

def register( name, email, password):
    userObject = User(name,email,password)
    query = "insert into users values (%s, %s, %s)"
    return cursor.execute(query, (userObject.name, userObject.email, userObject.password))

def login( email, password):
    for userObject in User.userList:
        if email == userObject.email:
            if password == userObject.password:
                return "Login successful"
    else:
        return "Invalid email/password"
class User:

    users = []

    def __init__( self, email, password, name ):
        self.email = email
        self.password = password
        self.name = name
    
    def __str__( self ):
        return str(self.__dict__)

def register():
    name = input("Enter name : ")
    email = input("Enter email : ")
    password = input("Enter password : ")
    user = User(email, password, name)
    User.users.append(user)
    print("Registered successfully !")
    for user in User.users:
        print(user)

def login():
    email = input("Enter email : ")
    password = input("Enter password : ")
    for user in User.users:
        if email == user.email:
            if password == user.password:
                print("Login succesful by", user)
                break
    else:
        print("Invalid username/password")

while True:
    print('''
    1. Login
    2. Register''')
    options = {'1' : login, '2' : register}
    choice = input("Enter your choice : ")
    options[choice]()
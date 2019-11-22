import sys
sys.path.append('..')
from controller import controller

def login():
    email = input("Enter your email : ")
    password = input("Enter password : ")
    print(controller.login(email,password))

def register():
    name = input("Enter your name : ")
    email = input("Enter your email : ")
    password = input("Enter password : ")
    result = controller.register(name, email, password)
    # for user in userList:
    #     print(user)
    print("Registered successfully..") if result == 1 else print("Registration failed") 

def errorHandler():
    print("Invalid choice !")

options = {"1" : login, "2" : register}

while True:
    print('''
    1. Login
    2. Register''')
    choice = input("Enter your choice : ")
    try:
        options.get(choice,errorHandler)()
    except BaseException as err:
        print(err)
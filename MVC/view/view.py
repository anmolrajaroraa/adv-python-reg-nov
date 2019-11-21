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
    userList = controller.register(name, email, password)
    for user in userList:
        print(user)
    print("Registered successfully..")

def errorHandler():
    print("Invalid choice !")

options = {"1" : login, "2" : register}

while True:
    print('''
    1. Login
    2. Register''')
    choice = input("Enter your choice : ")
    options.get(choice,errorHandler)()
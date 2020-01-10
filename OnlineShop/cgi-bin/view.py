#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import base

def registerSuccessful():
    base.header("Signup successful !!")
    base.footer()

def loginSuccessful(userid):
    base.header(f"Welcome {userid.title()} !!")
    base.footer()
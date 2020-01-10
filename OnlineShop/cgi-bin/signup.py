#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import cgi, model, view

fieldStorage = cgi.FieldStorage()
userid = fieldStorage.getvalue("userid")
email = fieldStorage.getvalue("email")
password = fieldStorage.getvalue("password")

result = model.signup(userid,email,password)

if result == 1:
    view.registerSuccessful()
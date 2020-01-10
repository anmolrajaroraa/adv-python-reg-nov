#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import cgi, model, view

fieldStorage = cgi.FieldStorage()
email = fieldStorage.getvalue("email")
password = fieldStorage.getvalue("password")

result = model.login(email,password)
view.loginSuccessful(result)
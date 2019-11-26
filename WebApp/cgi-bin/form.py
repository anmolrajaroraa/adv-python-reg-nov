#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
print("Content-type: text/html\r\n\r\n")

import cgi

fieldStorage = cgi.FieldStorage()
fullName = fieldStorage.getvalue('fullName')
email = fieldStorage.getvalue('email')
password = fieldStorage.getvalue('password')

print(f"Name : {fullName}")
print(f"Email : {email}")
print(f"Password : {password}")
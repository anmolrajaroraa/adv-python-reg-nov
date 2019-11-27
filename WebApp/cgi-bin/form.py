#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
print("Content-type: text/html\r\n\r\n")

import cgi, code

fieldStorage = cgi.FieldStorage()
fullName = fieldStorage.getvalue('fullName')
email = fieldStorage.getvalue('email')
password = fieldStorage.getvalue('password')

# print(f"Name : {fullName}")
# print(f"Email : {email}")
# print(f"Password : {password}")

print(f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Registration Successful</h1>
    <h2>Name : {fullName}</h2>
    <h2>Email : {email}</h2>
    <h2>Message : {code.msg}
</body>
</html>
''')
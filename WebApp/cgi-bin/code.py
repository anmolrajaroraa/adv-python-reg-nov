#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# print("Content-type: text/html\r\n\r\n")
# print("<!doctype html>")
# print("<html>")
# print("<head>")
# print("<title>Document</title>")
# print("</head>")
# print("<body>")
# print("<h1>This heading is printed by python</h1>")
# print("</body>")
# print("</html>")

msg = "This is a new style of writing html page"

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
    <h1>{msg}</h1>
</body>
</html>
''')
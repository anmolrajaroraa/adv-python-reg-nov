#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import base,cgi,product_base

fieldStorage = cgi.FieldStorage()
pid = int(fieldStorage.getvalue('pid'))

# products = base.getProducts()

base.header("<img src='https://rukminim1.flixcart.com/flap/844/140/image/0e5483e33a969756.jpg?q=50'>")

for product in base.products:
    if pid == product['product_id']:
        product_base.createHorizontalProduct(product)

base.footer()
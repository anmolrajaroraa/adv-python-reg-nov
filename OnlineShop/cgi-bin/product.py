#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import base,cgi,product_base

fieldStorage = cgi.FieldStorage()
pid = int(fieldStorage.getvalue('pid'))

# products = base.getProducts()

base.header()

for product in base.products:
    if pid == product['product_id']:
        product_base.createHorizontalProduct(product)

base.footer()
#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import base, DB, cgi

# products = base.getProducts()

fieldStorage = cgi.FieldStorage()
category = fieldStorage.getvalue('category')

if category != None:
    category = category.replace("%20", " ")
    category = category.upper()
    base.header(category)
    for product in DB.products:
        if product['product_category'] == category:
            base.createProduct(product)
else:
    base.header("Deals of the Day")
    for product in DB.products:
        base.createProduct(product)

base.footer()
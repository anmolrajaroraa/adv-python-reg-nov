#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import base

# products = base.getProducts()

base.header("Deals of the Day")

for product in base.products:
    base.createProduct(product)

base.footer()
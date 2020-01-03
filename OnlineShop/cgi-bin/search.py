#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import cgi, base

fieldStorage = cgi.FieldStorage()
query = fieldStorage.getvalue('q').lower()

intents = {
    "mobiles" : ['mobiles', 'mobile', 'phone', 'smartphone'],
    "televisions" : ['tv', 'smart tv', 'android tv', 'led tv', 'oled tv'],
    "refrigerators" : ['fridge', 'single door fridge', 'double door fridge'],
    "washing-machines" : ['washing machines', 'washing', 'automatic washing', 'washing machine'],
    "home-kitchen" : ['kitchen', 'home products', 'kitchen products', 'home kitchen']
}

for category in intents:
    if query in intents[category]:
        query = category
        break

# products = base.getProducts()

base.header()

for product in base.products:
    if query in product['product_category'] or query in product['product_brand'].lower() or query in product['product_name'].lower():
        base.createProduct(product)

base.footer()
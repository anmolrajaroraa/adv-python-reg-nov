#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import cgi, base, DB

fieldStorage = cgi.FieldStorage()
query = fieldStorage.getvalue('q').lower()

intents = {
    "mobiles" : ['mobiles', 'mobile', 'phone', 'smartphone'],
    "televisions" : ['tv', 'smart tv', 'android tv', 'led tv', 'oled tv'],
    "refrigerators" : ['fridge', 'single door fridge', 'double door fridge'],
    "washing-machines" : ['washing machines', 'washing', 'automatic washing', 'washing machine'],
    "home-kitchen" : ['kitchen', 'home products', 'kitchen products', 'home kitchen'],
    'watches' : ['watch', 'smartwatch', 'wrist watch', 'clock'],
    "men's fashion" : ['men fashion', 'mens', 'mens fashion', "man", "men"],
    "women's fashion" : ['women fashion', "fashion", 'women', "womens", "womens fashion", "woman"]
}

for category in intents:
    if query in intents[category]:
        query = category
        break

# products = base.getProducts()

base.header("Deals of the Day")

for product in DB.products:
    if query in product['product_sub_category'] or query in product['product_brand'].lower() or query in product['product_name'].lower() or query == product['product_category']:
        base.createProduct(product)

base.footer()
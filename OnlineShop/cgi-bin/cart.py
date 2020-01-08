#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import base, DB, cgi, model

fieldStorage = cgi.FieldStorage()
pid = fieldStorage.getvalue('pid')
if pid != None:
    model.addToCart(int(pid))

base.header("My Cart")

# print(f"<p>{DB.productsInCart}</p>")

# print(f"<p>{model.getProductsInCart()}</p>")

for product in DB.products:
    for x in model.getProductsInCart():
        if x[0] == product['product_id']:
            base.createProduct(product)

print('''
    <div class = "row" style="width:100%">
        <div class="col-md-2 offset-md-5" >
        <button class="btn btn-primary">Proceed to Payment</button>
        </div>
    </div>
''')

base.footer()
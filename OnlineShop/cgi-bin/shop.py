#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import base

products = base.getProducts()

base.header()

for product in products:
    print(f'''
        <div class="col-md-6 col-lg-4">
            <div class="card" style="width: 18rem; height: 28rem; margin-bottom: 20px; padding: 10px;">
                <div class="{product['product_category']}-parent">
                    <img class="{product['product_category']}" src="{product['product_image']}" class="card-img-top" alt="...">
                </div>
                <div class="card-body card-body-modified">
                    <h5 class="card-title">{product['product_brand'] + " " + product['product_name']}</h5>
                    <p class="card-text">₹{product['product_price']}</p>
                    <a href="#" class="btn btn-primary">View Product</a>
                </div>
            </div>
         </div>
    ''')

base.footer()
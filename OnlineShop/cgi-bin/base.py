import modals

def header(heading):
    print("Content-type: text/html\r\n\r\n")
    print(f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.0/css/bootstrap.min.css" integrity="sha384-SI27wrMjH3ZZ89r4o+fGIJtnzkAnFs3E4qz9DIYioCQ5l9Rd/7UAa8DHcaL8jkWt" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.0/js/bootstrap.min.js" integrity="sha384-3qaqj0lc6sV/qpzrc1N5DC6i1VRn/HyX4qdPaiEFbn54VjQBEU341pvjz7Dv3n6P" crossorigin="anonymous"></script>
        <script src="https://kit.fontawesome.com/cd00034d8b.js" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="../style.css">
    </head>
    <body style="color:black">

            <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
                    <a class="navbar-brand" href="shop.py">OnlineShop</a>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                    </button>
                
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav mr-auto" style="margin-top:0px">
                        <li class="nav-item">
                        <a class="nav-link" href="#" data-toggle="modal" data-target="#exampleModal" data-whatever="@getbootstrap">Login & Signup <span class="sr-only">(current)</span></a>
                        {modals.signupModal()}
                        {modals.loginModal()}
                        </li>
                        <li class="nav-item">
                        <a class="nav-link" href="cart.py">My Cart</a>
                        </li>
                        <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Categories
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <a class="dropdown-item" href="shop.py?category=men's%20fashion">Men</a>
                            <a class="dropdown-item" href="shop.py?category=women's%20fashion">Women</a>
                            <div class="dropdown-divider"></div>
                            <a class="dropdown-item" href="shop.py?category=electronics">Electronics</a>
                        </div>
                        </li>
                    </ul>
                    <form action="search.py" class="form-inline my-2 my-lg-0">
                        <input name="q" class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
                        <button class="btn btn-outline-light my-2 my-sm-0" type="submit">Search</button>
                    </form>
                    </div>
                </nav>

                <div class="container">
                    <h1>{heading}</h1>
                    <hr>
                    <div class="row">''')

def createProduct(product):
    print(f'''
        <div class="col-md-6 col-lg-4">
            <div class="card" style="width: 18rem; height: 28rem; margin-bottom: 20px; padding: 10px; border-radius: 10px;">
                <div class="{product['product_sub_category']}-parent">
                    <img class="{product['product_sub_category']}" src="{product['product_image']}" class="card-img-top" alt="...">
                </div>
                <div class="card-body card-body-modified">
                    <h6 class="card-title">{product['product_brand'] + " " + product['product_name']}</h6>
                    <p class="card-text">₹{product['product_price']}</p>
                    <a href="product.py?pid={product['product_id']}" class="btn btn-primary">View Product</a>
                </div>
            </div>
         </div>
    ''')

def footer():
    print('''    
                </div>
            </div>
</body>
</html>
''')
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

def createHorizontalProduct(product):
    
    query_brand = product['product_brand'].replace(' ', '%20')
    query_product = product['product_name'].replace(' ', '%20')
    response = urlopen(f"https://flipkart.com/search?q={query_brand}%20{query_product}")
    html = bs(response)
    a = html.find('a','_2cLu-l')
    # print(a)
    if a == None:
        a = html.find('a','_31qSD5')
    next_page = a['href']
    response = urlopen("https://flipkart.com" + next_page)
    html = bs(response)
    # print(next_page)
    # print(html.find('div','_1vC4OE _3qQ9m1').text)

    print(f'''
        <div class="card mb-3" style="width: 1200px; padding:10px;margin: 0 auto;">
            <div class="row no-gutters">
                <div class="col-md-3">
                <img src="{product['product_image']}" class="card-img" alt="...">
                </div>
                <div class="col-md-5 offset-md-1">
                <div class="card-body">
                    <h5 class="card-title">{html.find('span', '_35KyD6').text}</h5>
                    <div style="padding:5px;background-color:#26a541;color:white;display:inline;border-radius:10%">{html.find('div', 'hGSR34').text} <i class="fas fa-star"></i></div>
                    <p class="card-text" style="color:black;margin-top:10px;">{html.find('div','_1vC4OE _3qQ9m1').text}
                        &nbsp;
                        <small class="text-muted" style="text-decoration: line-through;">{html.find('div', '_3auQ3N _1POkHg').text}</small>
                        &nbsp;
                        <span class="text-muted">{html.find('div', 'VGWI6T _1iCvwn').text}</span>
                    </p>
                    
                    
                </div>
                </div>
                <div class="col-md-2 offset-md-1>
                </div>
            </div>
            </div>
    ''')

# createHorizontalProduct({
#             "product_id" : 1,
#             "product_brand" : "Realme",
#             "product_name" : "C2 (Diamond Blue, 32 GB)",
#             "product_image" : "https://rukminim1.flixcart.com/image/312/312/k0lbdzk0pkrrdj/mobile-refurbished/z/j/2/c2-16-u-rmx1945-realme-2-original-imaffnumygt8wgfx.jpeg?q=70",
#             "product_price" : 6499,
#             "product_mrp" : 7999,
#             "discount_percentage" : 18,
#             "product_rating" : 4.4,
#             "product_category" : "mobiles"
#         })
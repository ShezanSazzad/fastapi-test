from typing import Union

from fastapi import FastAPI

app = FastAPI()




class Category:
    def __init__(self, id, name, products):
        self.id = id
        self.name = name
        self.products = products

class Product:
    def __init__(self, id, product_name, barcode, manufacture_date, expiry_date):
        self.id = id
        self.product_name = product_name
        self.barcode = barcode
        self.manufacture_date = manufacture_date
        self.expiry_date = expiry_date


p1 = Product(1, "Kettle1" , 69, "12.6.2022" , "22.08.2089")
p2 = Product(2, "Kettle2" , 00, "12.6.2022" , "22.08.2089")
p3 = Product(3, "Kettle3" , 69, "12.6.2022" , "22.08.2089")
p4 = Product(4, "Kettle4" , 69, "12.6.2022" , "22.08.2089")
p5 = Product(5, "Kettle5" , 69, "12.6.2022" , "22.08.2089")
p6 = Product(6, "Kettle6" , 69, "12.6.2022" , "22.08.2089")
p7 = Product(7, "Kettle7" , 69, "12.6.2022" , "22.08.2089")
p8 = Product(8, "Kettle8" , 69, "12.6.2022" , "22.08.2089")

products = [p1,p2,p3,p4,p5,p6,p7,p8]

chips = Category(1, "Chips", products)
drinks = Category(2, "Drinks", products)
vegetables = Category(3, "Vegetables", products)

categories = [chips, drinks, vegetables]






@app.get("/")
def main_endpoint():
    return "Welcome to the shop!"


@app.get("/categories/")
def show_categories():
    return categories

@app.get("/categories/{category_id}")
def show_categories(category_id:int):        
    for category in categories:        
        if category.id == category_id:
            return category
    return "category not on the system"
    




@app.get("/products/")
def show_categories():
    return products


@app.get("/products/{product_id}")
def show_product(product_id : int):
    for product in products:
        if product.id == product_id:
            return product
    return "product not on the system"

# Show the product name only inside a category
@app.get("/categories/{category_id}/products_names")
def show_product_names_under_category(category_id:int):
    result = []    
    for category in categories:
        if (category.id == category_id):
            for product in category.products:                
                result.append(product.product_name)            
    return result



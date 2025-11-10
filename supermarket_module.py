import re
from datetime import date, datetime
import pickle

product_list = []

def name_validator(name):
    if re.match(r"^[a-zA-Z\s]{2,20}$", name):
        return name
    else:
        raise ValueError("Name must be a string")

def brand_validator(brand):
    if re.match(r"^[a-zA-Z\s]{2,20}$", brand):
        return brand
    else:
        raise ValueError("Brand must be a string")

#def id_validator(id_number):
    if type(id_number) == int and 999999999<id_number<10000000000 :
        return id_number
    else:
        raise ValueError("Id Number must contain ten digits!!!")

def price_validator(price):
    if type(price) == float and price > 0:
        return price
    else:
        raise ValueError("Price must be a positive number")

def quantity_validator(quantity):
    if type(quantity) == int and quantity > 0:
        return quantity
    else:
        raise ValueError("Quantity must be a positive number")

def expire_validator(expire_date):
    if type(expire_date) != date and expire_date >= date.today():
        raise ValueError("Expiration date must be YYYY-MM-DD.")

def creat_products_and_validate(id_number ,name , brand , quantity , price , expiration_date):
    #id_validator(id_number)
    name_validator(name)
    brand_validator(brand)
    quantity_validator(quantity)
    price_validator(price)
    # تبدیل تاریخ از رشته به تاریخ
    expire_date = datetime.strptime(expiration_date, "%Y-%m-%d").date()
    expire_validator(expire_date)

    product = {
        "id_number": id_number,
        "name": name,
        "brand": brand,
        "quantity": quantity,
        "price": price,
        "expire_date": expire_date
    }
    return product

def calculate_total(product_list):
    # If there is no product available show this message
    if not product_list:
        raise ValueError("No Products", "There are no products saved.")


    total = 0

    for product in product_list:
        total = total + product['quantity'] * product['price']
    return total

def save_to_file(product_list):
    file = open("supermarket.dat", "wb")
    pickle.dump(product_list, file)
    file.close()



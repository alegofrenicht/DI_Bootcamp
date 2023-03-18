import json


def retrieve_all_products():
    with open('jsonformatter.json', 'r') as file_obj:
        all_products = json.load(file_obj)
    return all_products


def retrieve_requested_product(product_id):
    requested_product = [product for product in retrieve_all_products() if product['ProductId'] == product_id]
    return requested_product[0]

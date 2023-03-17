import json

def load_database():
    with open('product_db.json', 'r') as file_obj:
        data = json.load(file_obj)
    return data

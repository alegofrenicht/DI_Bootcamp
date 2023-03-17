from flask import Flask, render_template
from database_manager import load_database

app = Flask(__name__)
data = load_database()


@app.route('/')
def main():
    html = render_template('home_page.html')
    return html


@app.route('/home')
def home_page():
    html = render_template('home_page.html')
    return html


@app.route('/products')
def products_page():
    html = render_template('products.html', products=data)
    return html


@app.route('/products/<product_id>')
def product_details(product_id):
    product = [product for product in data if product['ProductId'] == product_id]
    print(product[0])
    html = render_template('product_page.html', product=product[0])
    return html


app.run()

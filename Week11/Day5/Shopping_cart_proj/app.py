import flask
from flask import Flask, render_template
import products_data

app = Flask(__name__)
data = products_data.retrieve_all_products()
cart_items = []

@app.route('/')
def main_page():
    html = render_template('main.html')
    return html


@app.route('/home')
def home():
    html = render_template('main.html')
    return html


@app.route('/products')
def products_page():
    html = render_template('products_page.html', products=data)
    return html


@app.route('/add_product_to_cart/<item>')
def add(item):
    cart_items.append(products_data.retrieve_requested_product(item))
    html = render_template('products_page.html', products=data)
    return html

@app.route('/delete_product_from_cart/<item>')
def delete(item):
    cart_items.remove(products_data.retrieve_requested_product(item))
    html = render_template('cart.html', items=cart_items)
    return html


@app.route('/cart')
def cart():
    html = render_template('cart.html', items=cart_items)
    return html


app.run()
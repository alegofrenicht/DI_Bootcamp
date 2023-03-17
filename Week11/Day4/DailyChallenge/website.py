from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    html = render_template('main_template.html')
    return html


@app.route('/<color>')
def colors(color):
    html = render_template('color.html', color=color)
    return html


app.run()
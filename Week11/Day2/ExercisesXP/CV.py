import flask
from flask import render_template

app = flask.Flask(__name__)


@app.route('/')
def index():

    html = render_template('template.html')
    return html


# if __name__ == "__main__":
# app.run(debug=True, port=5000)

if __name__ == "__main__":
    app.run()
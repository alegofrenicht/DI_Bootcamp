import markdown
import flask
from flask import render_template

app = flask.Flask(__name__)


@app.route('/')
def home_page():
    return flask.redirect(flask.url_for('exercises'))


@app.route('/in-this-chapter')
def lesson():
    with open('in-this-chapter.md') as ch:
        md = ch.read()
        html = markdown.markdown(md)
    return html


@app.route('/exercises')
def exercises():
    with open('exercises.md') as ch:
        md = ch.read()
        html = markdown.markdown(md)
    return html


if __name__ == '__main__':
    app.run()

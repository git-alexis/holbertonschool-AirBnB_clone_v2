#!/usr/bin/python3
"""This module starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns a string when the route / is hit"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a string when the route /hbnb is hit"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_and_text(text):
    """Returns a string when the route /c/ and a text is hit"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

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


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
def python_and_text(text):
    """
    Returns a string or a default value ('is cool')
    when the route /python/ and a text or nothing is hit
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_and_n(n):
    """Returns a string when the route /c/ and a text is hit"""
    return 'number {}'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

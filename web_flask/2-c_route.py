#!/usr/bin/python3


""" flask module """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index0():
    """ index 0 """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def index1():
    """ index 1 """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cvalue(text):
    """ cvalue """
    return "C %s" % text


if __name__ == "__main__":
    app.run()

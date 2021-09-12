#!/usr/bin/python3
'''Flask task 1 Module'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    '''Print Hello HBNB'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Print HBNB'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''Print C with the variable text'''
    res = text.replace("_", " ")
    return 'C {}'.format(res)

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text="is_cool"):
    '''Print Python with the variable text'''
    res = text.replace("_", " ")
    return 'Python {}'.format(res)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

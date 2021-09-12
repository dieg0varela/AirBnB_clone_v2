#!/usr/bin/python3
'''Flask task 1 Module'''
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''Print N is a number'''
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''Print N in a HTML Template'''
    return render_template('/5-number.html', number=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

#!/usr/bin/python3
'''Flask task 1 Module'''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''Print StatesList'''
    return render_template('/7-states_list.html',
                           states=storage.all(State).values())


@app.teardown_appcontext
def teardown(f):
    '''Execute each time after an method'''
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

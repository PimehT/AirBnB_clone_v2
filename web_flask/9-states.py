#!/usr/bin/python3
""" starts a flask web application """
from flask import Flask, render_template
from models import *
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    storage.close()


@app.route('/states', strict_slashes=False)
def list_states():
    states = storage.all(State).values()
    return render_template('states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def show_state(id):
    state = storage.get(State, id)
    if state:
        return render_template('state.html', state=state)
    else:
        return render_template('not_found.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
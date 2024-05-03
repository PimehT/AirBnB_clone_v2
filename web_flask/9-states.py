#!/usr/bin/python3
""" starts a flask web application """
from flask import Flask, render_template
from models import *
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ Teardown app context """
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """ States list route """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.route("/states/<id>", strict_slashes=False)
def state(id):
    """ State route with cities listed """
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('not_found.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

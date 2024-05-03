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


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    """ Integrate listing of states into 6-index.html file """
    return render_template('10-hbnb_filters.html', states=storage.all(State),
                           amenities=storage.all(Amenity))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

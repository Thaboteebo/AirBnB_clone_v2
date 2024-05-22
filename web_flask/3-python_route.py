#!/usr/bin/python3
"""
start Flask application
"""

from flask import Falsk
app = Falsk(__name__)


@app.route('/', strict_slashes=False)
def index():
    """return Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return HBNB"""
    return 'HBNB'

@app.route'/c/text>', strict_slashes=False)
def cisfun(text):
    """display “C ” flollowed bt the value of the text variable"""
    return 'c' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Pyhton ”, followed by the value of the text variable"""
    return 'Pyhton ' + text.replace('_'. ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
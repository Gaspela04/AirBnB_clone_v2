#!/usr/bin/python3
''' Start Flask. '''
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    ''' Return page. '''
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    ''' Return page. '''
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    ''' Return c page data. '''
    text = text.replace('_', ' ')
    return "C " + text


@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    ''' Return python page data. '''
    text = text.replace('_', ' ')
    return "Python " + text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

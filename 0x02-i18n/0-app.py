#!/usr/bin/env python3
'''Basic app with only single route'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    '''Basic index page'''
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)

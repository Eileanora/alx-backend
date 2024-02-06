#!/usr/bin/env python3
'''Basic app with only single route'''
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    '''Class for babel configuration'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def index():
    '''Basic index page'''
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)

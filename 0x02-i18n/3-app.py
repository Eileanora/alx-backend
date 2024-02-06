#!/usr/bin/env python3
'''Basic app with only single route'''
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    '''Class for babel configuration'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    '''Gets the locale language'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''Basic index page'''
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)

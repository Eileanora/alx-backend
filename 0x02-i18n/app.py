#!/usr/bin/env python3
'''Basic app with only single route'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz


class Config:
    '''Class for babel configuration'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    '''Mocks logged in user'''
    ID = request.args.get('login_as')
    if ID and int(ID) in users:
        return users[int(ID)]
    return None


@app.before_request
def before_request():
    '''Before request'''
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    '''Gets the locale language'''
    url_locale = request.args.get('locale')
    if url_locale and url_locale in app.config['LANGUAGES']:
        return url_locale

    user_locale = g.user['locale']
    if user_locale and user_locale in app.config['LANGUAGES']:
        return user_locale

    header_locale = request.headers.get('locale', None)
    if header_locale and header_locale in app.config['LANGUAGES']:
        return header_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    '''Gets the timezone'''
    url_timezone = request.args.get('timezone', None)
    if url_timezone:
        try:
            return pytz.timezone(url_timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        user_timezone = g.user['timezone']
        if user_timezone:
            try:
                return pytz.timezone(user_timezone)
            except pytz.exceptions.UnknownTimeZoneError:
                pass

    return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])


@app.route('/')
def index():
    '''Basic index page'''
    g.time = format_datetime()
    return render_template('index.html', user=g.user)


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)

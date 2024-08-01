#!/usr/bin/env python3
"""Basic babel setup"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


class Config:
    """Config class
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Get locale function
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.context_processor
def inject_locale():
    """Inject locale into the function"""
    return dict(get_locale=get_locale)


@app.route('/')
def index() -> str:
    """Default root
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)

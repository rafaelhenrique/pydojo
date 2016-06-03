from flask import Flask

from pydojo import config
from pydojo.core import core_blueprint
from pydojo.ext import csrf, migrate, db


def create_app(config=config.ProductionConfig):
    app = Flask("pydojo")
    app.config.from_object(config)

    register_blueprints(app)
    register_errorhandlers(app)
    register_jinja_env(app)
    register_extensions(app)

    return app


def register_blueprints(app):
    app.register_blueprint(core_blueprint, url_prefix='/')


def register_errorhandlers(app):
    def render_error(e):
        if e.code == 400:
            return 'Bad request.', 400
        elif e.code == 404:
            return 'Not found.', 404
        elif e.code == 500:
            return 'Internal server error', 500

    for e in [400, 404, 500]:
        app.errorhandler(e)(render_error)


def register_jinja_env(app):
    pass


def register_extensions(app):
    csrf.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

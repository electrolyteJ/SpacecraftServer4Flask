import os
from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
import logging
from logging.handlers import SMTPHandler

'''
author:hawks jamesf
'''

mail_handler = SMTPHandler(
    mailhost='127.0.0.1',
    fromaddr='server-error@example.com',
    toaddrs=['hawksjamesf@gmail.com'],
    subject='Application Error'
)
mail_handler.setLevel(logging.ERROR)
mail_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'app.sqlite'))
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_pyfile(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    sentry_sdk.init(
        dsn="https://c659bb3641e14a86b54a0d3db91ff7ea@sentry.io/2495776",
        integrations=[FlaskIntegration()]
    )
    if not app.debug: app.logger.addHandler(mail_handler)
    # @app.route('/')
    # def hello_world():
    #     return 'Hello World!'

    from . import db
    db.oncreate_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    return app

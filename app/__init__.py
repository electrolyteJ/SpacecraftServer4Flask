import os

from flask import Flask
from app.util import l
from app import api, storage
from app.config import DevelopmentConfig


def create_app(config_file=None, config_object=DevelopmentConfig):
    app = Flask(__name__, instance_relative_config=True)
    # 优先从文件区配置，有利于动态改变正在运行的app配置
    if config_file:
        l.i("读取config_file")
        app.config.from_pyfile(config_file)
    else:
        # 1.cfg =import_string('config.DevelopmentConfig')
        # app.config.from_object(cfg)
        # 2 app.config.from_object('config.DevelopmentConfig')
        l.i("读取config_object")
        app.config.from_object(config_object)
    # app.config.from_envvar()
    # app.config.from_json()
    # app.config.update()
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # sentry_sdk.init(
    #     dsn="https://c659bb3641e14a86b54a0d3db91ff7ea@sentry.io/2495776",
    #     integrations=[FlaskIntegration()]
    # )
    api.init(app)
    l.init(app)
    storage.init(app)
    return app

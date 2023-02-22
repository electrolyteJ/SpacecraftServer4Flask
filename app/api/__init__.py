from flask import Flask, render_template
from flask_restful import Api

from app.api import user


def init(app: Flask):
    api = Api(app)
    api.add_resource(user.UserApi, "/api/user", "/api/user/<int:user_id>/<string:action>", "/api/user/<string:action>",
                     "/api/user/<int:user_id>", endpoint='user')

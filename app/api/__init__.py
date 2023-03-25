from flask import Flask, render_template
from flask_restful import Api

from app.api import user,passport


def init(csrf_protect,app: Flask):
    api = Api(app, decorators=[csrf_protect.exempt])
    # api = Api(app)
    api.add_resource(user.UserApi, "/api/user", "/api/user/<int:user_id>/<string:action>", "/api/user/<string:action>",
                     "/api/user/<int:user_id>", endpoint='user')
    api.add_resource(passport.PassportAPI, '/api/passport/', '/api/passport/<string:action>', endpoint='passport')

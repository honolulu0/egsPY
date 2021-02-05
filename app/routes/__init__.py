# coding=utf-8
from flask import session, request

from app.routes.optimizationRoute import userRoute

print('routes')


def init(app):
    global_filter(app)
    register_blueprint(app)


def global_filter(app):
    @app.before_request
    def before_request():
        print(request.path)
        if session.get('user'):
            print('session-->' + session.get('user'))
        pass


def register_blueprint(app):
    app.register_blueprint(userRoute, url_prefix='/optimization')

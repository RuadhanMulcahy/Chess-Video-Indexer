"""
This module contains a blueprint for the api version route.
e.g. the /v1/ prefix for all routes as part of api v1.
"""
from flask import Blueprint

from api.mysql import mysql_routes

api_version = Blueprint('api_version', __name__)
api_version.register_blueprint(mysql_routes, url_prefix='/v1')

@api_version.route('/v1')
def version_one():
    """
    Default Route for CVI Monitor Service API v1.
    """
    return 'API v1 Default Route.'

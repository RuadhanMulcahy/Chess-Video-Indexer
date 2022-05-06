"""
CVI Data MySQL API. Defines routes for our
interactions with MySQL databases.
"""
from flask import Blueprint
from dotenv import dotenv_values

from operators.mysql import MySQL

config = dotenv_values(".env")

mysql_routes = Blueprint('mysql_routes', __name__)

@mysql_routes.route('/mysql/test')
def test_database_connection():
    """
    MySQL Operator call ->
    Test database connectivity.
    :return: database_connectivity_status
    :rtype: str
    """
    mysql_operator = MySQL()
    return mysql_operator.test_database_connection()

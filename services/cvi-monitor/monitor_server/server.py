"""
This defines the CLI options for the monitor service.
"""
from flask import Flask

from monitor_server.etc import logging_utils
from monitor_server.operators.hello_world import HelloWorld

app = Flask(__name__)

@app.route('/')
def hello():
    """
    Temporary Default Route
    """
    logging_utils.initialize_logging(verbose=True)
    hello_world_operator = HelloWorld()
    return hello_world_operator.say_hello()

def server_main():
    """
    Entrypoint for Flask Server
    """
    app.run(host='0.0.0.0', port=5000)

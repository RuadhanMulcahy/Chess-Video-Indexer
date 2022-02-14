"""
This defines the CLI options for the monitor service.
"""
import logging
from flask import Flask

from monitor_server.etc import logging_utils
from monitor_server.operators.hello_world import HelloWorld

app = Flask(__name__)

@app.route('/')
def hello():
    logging_utils.initialize_logging(verbose=True)
    logging.info('TEST!')
    return 'Hello, World!'

def server_main():
    app.run(host='0.0.0.0', port=5000)
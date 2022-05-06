"""
Entrypoint Module for CVI Data Service.
"""
from flask import Flask

from api.api_version import api_version

app = Flask(__name__)
app.register_blueprint(api_version)

@app.route('/')
def default_route():
    """
    Root Default API Route for the CVI Data Service.
    """
    return 'Default Route, Please Specify API Version.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)

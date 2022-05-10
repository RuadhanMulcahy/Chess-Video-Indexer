"""
Entrypoint Module for CVI Monitor Service.
"""
from flask import Flask
from cron import CadenceType, Cron

from api.api_version import api_version

app = Flask(__name__)
app.register_blueprint(api_version)

@app.route('/')
def default_route():
    """
    Root Default API Route for the CVI Monitor Service.
    """
    return 'Default Route, Please Specify API Version.'

def test_job():
    """
    Temporary test function.
    """
    print('Test Job for APScheduler.')

if __name__ == '__main__':
    cron = Cron()
    cron.schedule_job(test_job, cadence_type=CadenceType.HOURS)
    cron.sched.start()
    app.run(host='0.0.0.0', port=3000, debug=False)

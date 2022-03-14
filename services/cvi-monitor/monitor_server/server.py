"""
This defines the CLI options for the monitor service.
"""
import logging
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

from monitor_server.etc import logging_utils
from monitor_server.operators.youtube import Youtube

def scan_channel():
    logging.info('Running Scan Channel Job!')
    youtube_operator = Youtube()
    there_are_new_videos = youtube_operator.check_for_new_videos()
    if there_are_new_videos:
        for video in youtube_operator.videos:
            print(video)

cron = BackgroundScheduler(daemon=True)
cron.add_job(scan_channel, 'interval', id='cvi-monitor-cron', seconds=300)
cron.start()

app = Flask(__name__)

@app.route('/')
def default_route():
    """
    Default route for the CVI Monitor server.
    This will return information about the cron (interval time + next scheduled run)
    """
    logging_utils.initialize_logging(verbose=True)
    response = cron.get_job('cvi-monitor-cron')
    return str(response)

def server_main():
    """
    Entrypoint for Flask Server
    """
    app.run(host='0.0.0.0', port=5000)

"""
CVI Monitor Youtube API Interface. Defines routes for our
specific interactions with the Youtube API.
"""
from flask import Blueprint
from dotenv import dotenv_values

from operators.youtube import Youtube

config = dotenv_values(".env")

youtube_routes = Blueprint('youtube_routes', __name__)

@youtube_routes.route('/youtube/channel_stats/<channel_id>')
def get_channel_statistics(channel_id):
    """
    Youtube Operator call ->
    Get Channel Statistics by Channel ID.
    :param channel_id:
    :return youtube_channel_stats:
    :rtype str:
    """
    youtube = Youtube(config['YOUTUBE_API_KEY'])
    return youtube.get_channel_statistics(channel_id)

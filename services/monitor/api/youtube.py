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
    :return: youtube_channel_stats
    :rtype: str
    """
    youtube = Youtube(config['YOUTUBE_API_KEY'])
    return youtube.get_channel_statistics(channel_id)

@youtube_routes.route('/youtube/recent_videos/<channel_id>')
def get_recent_videos(channel_id):
    """
    Youtube Operator call ->
    Get last 5 videos by Channel ID in order of upload date.
    Returns a dict where the key is upload date and value is video url.
    :param channel_id:
    :return: dict_of_recent_video_urls
    :rtype: dict
    """
    recent_videos = {}
    youtube = Youtube(config['YOUTUBE_API_KEY'])
    response = youtube.get_recent_videos(channel_id)
    for item in response['items']:
        recent_videos[item['snippet']['publishedAt']] = f'https://www.youtube.com/watch?v={item["id"]["videoId"]}'
    return { 'items': recent_videos }

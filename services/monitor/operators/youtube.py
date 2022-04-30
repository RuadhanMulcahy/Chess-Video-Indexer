"""
Module to house the Youtube Operator to interact with youtubes API.
"""
from googleapiclient.discovery import build

class Youtube():
    """
    CVI Monitor Service's own defined Youtube object to interact
    with youtubes API. This will use googles python api client to
    interact with youtube and process the returning data.
    """
    def __init__(self, api_key):
        self.api = build('youtube', 'v3', developerKey=api_key)

    def get_channel_statistics(self, channel_id):
        """
        Get Channel Statistics by Channel ID.
        :param channel_id:
        :return: youtube_channel_stats
        :rtype: str
        """
        request = self.api.channels().list(
            part='statistics',
            id=channel_id
        )
        return request.execute()

    def get_recent_videos(self, channel_id):
        """
        Get last 5 videos by Channel ID in order of upload date.
        :param channel_id:
        :return: youtube_channel_recent_videos
        :rtype: str
        """
        request = self.api.search().list(
            part="snippet",
            channelId=channel_id,
            maxResults=5,
            order="date"
        )
        return request.execute()

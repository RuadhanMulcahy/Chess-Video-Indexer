# Module to house the Youtube API operator.

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class Youtube:
    DEVELOPER_KEY = 'AIzaSyDw6gmdZhDgbzHcggtNTyKeH8yBXV5xe_w'
    API_SERVICE_NAME = 'youtube'
    API_VERSION = 'v3'

    def __init__(self):
        self.videos = None
        self.options = Youtube.Options(None, max_results=10)
    
    def search(self, options=None):
        if options is None:
            options = self.options

        youtube = build(Youtube.API_SERVICE_NAME,
                        Youtube.API_VERSION,
                        developerKey=Youtube.DEVELOPER_KEY)

        search_response = youtube.search().list(
            q=options.query,
            part='id,snippet',
            maxResults=options.max_results
        ).execute()

        videos = []
        channels = []
        playlists = []

        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                videos.append('%s (%s)' % (search_result['snippet']['title'],
                                            search_result['id']['videoId']))
            elif search_result['id']['kind'] == 'youtube#channel':
                channels.append('%s (%s)' % (search_result['snippet']['title'],
                                            search_result['id']['channelId']))
            elif search_result['id']['kind'] == 'youtube#playlist':
                playlists.append('%s (%s)' % (search_result['snippet']['title'],
                                                search_result['id']['playlistId']))
        
        return videos, channels, playlists
    
    class Options:
        def __init__(self, query, max_results):
            self.query = query
            self.max_results = max_results

if __name__ == '__main__':
    yt_api = Youtube()
    yt_api.options.query = 'test'
    videos, channels, playlists = yt_api.search()
    print('Videos:\n', videos)
    print('Channels:\n', channels)
    print('Playlists:\n', playlists)
"""
Module for handling RSS feeds
"""
import logging

import feedparser

class FeedHandler():
    """RSS Feed Handler Class"""
    def __init__(self, source: str):
        self.source = source

    def parse_source(self):
        """Temporary say hello method"""
        logging.info('About to say hello!')
        logging.debug('This is a debug log!')
        my_feed = feedparser.parse(self.source)
        return my_feed



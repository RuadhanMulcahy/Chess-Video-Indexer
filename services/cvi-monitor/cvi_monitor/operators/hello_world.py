"""
Temporary hello world module.
"""
import logging

class HelloWorld():
    """Temporary hello world class"""
    @staticmethod
    def say_hello():
        """Temporary say hello method"""
        logging.info('About to say hello!')
        logging.debug('This is a debug log!')
        return 'Hello World!'

    @staticmethod
    def say_goodbye():
        """Temporary say goodbye method"""
        logging.info('About to say goodbye!')
        return 'Goodbye World!'

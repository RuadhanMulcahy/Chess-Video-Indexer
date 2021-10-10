"""
Utilities file to store logging functions
"""
import logging


def initialize_logging(verbose=False):
    """
    Get the root logger and set the handlers and formatters.
    :param verbose: Flag to set logging level to debug.
    """
    logger = logging.getLogger('')
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        console = logging.StreamHandler()
        formatter = logging.Formatter(
            '[%(levelname)s][%(filename)s:%(funcName)s:%(lineno)s][%(asctime)s] '
            '%(message)s')
        console.setFormatter(formatter)
        console.setLevel(logging.INFO)
        logger.addHandler(console)
    set_logging_verbosity_level(logger, verbose)


def set_logging_verbosity_level(logger, verbose):
    """
    Sets the verbosity level of the specified logger handler depending on the verbose
    option passed in.
    :param logger: The logger to set the handler level for
    :param verbose: True or False
    """
    console = logger.handlers[0]
    if verbose:
        console.setLevel(logging.DEBUG)
        logging.debug("Logging Level set to DEBUG")
    else:
        console.setLevel(logging.INFO)
        logging.info("Logging Level set to INFO")

"""
This defines the CLI options for the monitor service.
"""
import click

from cvi_monitor.etc import logging_utils
from cvi_monitor.operators.hello_world import HelloWorld


def log_verbose_option(func):
    """A decorator for the log verbose command line argument."""
    return click.option('-v', '--verbose', type=click.BOOL, is_flag=True, required=False,
                        help='Increase log output verbosity.')(func)


@click.group()
def cli_main():
    """
    The entry-point to the Chess Video Indexer monitor service.
    See the available options below.
    """


@cli_main.command()
@log_verbose_option
def hello_world(verbose):
    """
    Hello world placeholder command line to act as a temporary
    entrypoint to the Chess Video Indexer monitor service.
    :param verbose:
    """
    logging_utils.initialize_logging(verbose)
    hello_world_operator = HelloWorld()
    print(hello_world_operator.say_hello())

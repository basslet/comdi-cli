"""
Helper functions.
"""
import logging

import coloredlogs

log_level = None  # pylint: disable=invalid-name


def get_colored_logger(name=__name__, verbosity=None):
    """
    Return a logger with the specified name, creating it if necessary.
    If no name is specified, return the root logger.
    Enable colored terminal output.

    Args:
        name: Logger name. Defaults to __name__.
        verbosity: Logging level. Defaults to None.

    Returns:
        Logger
    """

    global log_level  # pylint: disable=global-statement

    if verbosity is not None:
        if log_level is None:
            log_level = verbosity
        else:
            raise RuntimeError("Verbosity has already been set.")

    shortname = name  # name.replace("yapytr.", "")

    logger = logging.getLogger(shortname)

    # no logging of libs
    logger.propagate = False

    if log_level == "debug":
        fmt = "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"

        datefmt = "%Y-%m-%d %H:%M:%S%z"
    else:
        fmt = "%(asctime)s %(message)s"

        datefmt = "%H:%M:%S"

    fs = {
        "asctime": {"color": "green"},
        "hostname": {"color": "magenta"},
        "levelname": {"color": "red", "bold": True},
        "name": {"color": "magenta"},
        "programname": {"color": "cyan"},
        "username": {"color": "yellow"},
    }

    ls = {
        "critical": {"color": "red", "bold": True},
        "debug": {"color": "green"},
        "error": {"color": "red"},
        "info": {},
        "notice": {"color": "magenta"},
        "spam": {"color": "green", "faint": True},
        "success": {"color": "green", "bold": True},
        "verbose": {"color": "blue"},
        "warning": {"color": "yellow"},
    }

    coloredlogs.install(
        level=log_level,
        logger=logger,
        fmt=fmt,
        datefmt=datefmt,
        level_styles=ls,
        field_styles=fs,
    )

    return logger

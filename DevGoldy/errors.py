import logging
from devgoldyutils.errors import DevGoldyUtilsError

class DevGoldyException(DevGoldyUtilsError):
    def __init__(self, message: str, logger: logging.Logger = None):
        super().__init__(message, logger)

class OSNotSupported(DevGoldyException):
    """Raises when the operating system or the specific Linux distro is not supported."""
    def __init__(self, logger: logging.Logger = None):
        super().__init__(
            "Sorry, this command is not supported yet on this operating system or linux distro.", 
            logger = logger
        )
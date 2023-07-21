import logging
from typing import Final
from devgoldyutils import add_custom_handler, Colours

dev_goldy_logger = add_custom_handler(
    logger = logging.getLogger(Colours.GREY.apply("Dev Goldy")), # TODO: Change colour to a blueish purple when that is available.
    level = logging.DEBUG
)

__version__: Final[str] = "1.3.2"
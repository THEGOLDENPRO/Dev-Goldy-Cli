import os
import sys

from . import dev_goldy
from ... import errors

@dev_goldy.group(invoke_without_command = False)
def reload():
    """Allows you reload stuff in your operating system. Use with CAUTION."""
    ...

@reload.command()
def gui():
    """Command for reloading desktop environment."""
    if sys.platform == "linux":

        if os.environ.get("KDE_FULL_SESSION") == "true": # KDE
            return os.system("killall plasmashell && kstart5 plasmashell")

    raise errors.OSNotSupported()

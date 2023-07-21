import os

from . import dev_goldy

@dev_goldy.group(invoke_without_command = False)
def fix():
    """Fixes I've compiled for various things."""
    ...

@fix.command()
def unlock():
    """Command for unlocking KDE lock screen when it fucking blows up."""
    return os.system("loginctl unlock-session 2")
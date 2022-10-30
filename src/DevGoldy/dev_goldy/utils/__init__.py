class ShellInterface():
    """The base class of shell based interfaces in dev goldy cli."""
    def __init__(self):
        pass

    def run(self) -> None:
        """Runs the command and returns process in some way."""
        return None

from .powershell import PowerShell
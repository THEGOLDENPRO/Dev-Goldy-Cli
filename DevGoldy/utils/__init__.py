from abc import ABC, abstractmethod

class ShellInterface(ABC):
    """The base class of shell based interfaces in dev goldy cli."""
    def __init__(self):
        pass
    
    @abstractmethod
    def run(self) -> None:
        """Runs the command and returns process in some way."""
        ...

from .powershell import PowerShell
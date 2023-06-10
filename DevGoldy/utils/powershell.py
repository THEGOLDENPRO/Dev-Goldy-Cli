import sys
import subprocess

from . import ShellInterface

class PowerShell(ShellInterface):
    """Microsoft Powershell interface."""
    def __init__(self, cmd:str):
        self.process = subprocess.Popen(["powershell", "-Command", cmd], stdout=sys.stdout)
        super().__init__()

    def run(self) -> subprocess.Popen:
        self.process.communicate()
        return self.process
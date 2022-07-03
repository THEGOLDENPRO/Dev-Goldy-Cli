import sys, os

from . import click, utils, devgoldy

@devgoldy.command()
@click.argument('option')
def usb(option:str):
    if option == "all":
        if sys.platform == "win32":
            utils.powershell.run("Get-PnpDevice -PresentOnly | Where-Object { $_.InstanceId -match '^USB' }")

        if sys.platform == "linux":
            os.system("lsusb")
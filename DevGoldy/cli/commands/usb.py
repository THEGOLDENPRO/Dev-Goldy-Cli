import os
import sys

import click
from click import Context

from . import dev_goldy
from ... import utils, errors

@dev_goldy.group(invoke_without_command = True)
@click.pass_context
def usb(ctx:Context):
    """Allows you to list all and specific usb devices."""
    if ctx.invoked_subcommand is not None:
        pass
    else:
        all.invoke(ctx)

@usb.command()
def all():
    if sys.platform == "win32":
        return utils.PowerShell("Get-PnpDevice -PresentOnly | Where-Object { $_.InstanceId -match '^USB' }").run()

    elif sys.platform == "linux":
        return os.system("lsusb")

    raise errors.OSNotSupported()
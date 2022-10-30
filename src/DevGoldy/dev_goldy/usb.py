import sys, os

from click import Context

from . import click, utils, devgoldy

@devgoldy.group(invoke_without_command=True)
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
        utils.PowerShell("Get-PnpDevice -PresentOnly | Where-Object { $_.InstanceId -match '^USB' }").run()

    if sys.platform == "linux":
        os.system("lsusb")
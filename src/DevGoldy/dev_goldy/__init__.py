import click
import devgoldyutils

console = devgoldyutils.Console()

@click.group(invoke_without_command=True)
@click.pass_context
def devgoldy(ctx):
    if ctx.invoked_subcommand is None:
        print("""
██████╗░███████╗██╗░░░██╗  ░██████╗░░█████╗░██╗░░░░░██████╗░██╗░░░██╗
██╔══██╗██╔════╝██║░░░██║  ██╔════╝░██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝
██║░░██║█████╗░░╚██╗░██╔╝  ██║░░██╗░██║░░██║██║░░░░░██║░░██║░╚████╔╝░
██║░░██║██╔══╝░░░╚████╔╝░  ██║░░╚██╗██║░░██║██║░░░░░██║░░██║░░╚██╔╝░░
██████╔╝███████╗░░╚██╔╝░░  ╚██████╔╝╚█████╔╝███████╗██████╔╝░░░██║░░░
╚═════╝░╚══════╝░░░╚═╝░░░  ░╚═════╝░░╚════╝░╚══════╝╚═════╝░░░░╚═╝░░░
        """)

    else:
        print(console.BLUE(f"Running command {ctx.invoked_subcommand}..."))
        print("")
    
from . import utils
from . import start, usb
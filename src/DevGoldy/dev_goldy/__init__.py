import click
import devgoldyutils

try:
    from .. import info
except ValueError:
    import info

console = devgoldyutils.Console()

@click.group(invoke_without_command=True)
@click.pass_context
def devgoldy(ctx:click.Context):
    if ctx.invoked_subcommand is None:
        print(f"""
██████╗░███████╗██╗░░░██╗  ░██████╗░░█████╗░██╗░░░░░██████╗░██╗░░░██╗
██╔══██╗██╔════╝██║░░░██║  ██╔════╝░██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝
██║░░██║█████╗░░╚██╗░██╔╝  ██║░░██╗░██║░░██║██║░░░░░██║░░██║░╚████╔╝░
██║░░██║██╔══╝░░░╚████╔╝░  ██║░░╚██╗██║░░██║██║░░░░░██║░░██║░░╚██╔╝░░
██████╔╝███████╗░░╚██╔╝░░  ╚██████╔╝╚█████╔╝███████╗██████╔╝░░░██║░░░
╚═════╝░╚══════╝░░░╚═╝░░░  ░╚═════╝░░╚════╝░╚══════╝╚═════╝░░░░╚═╝░░░

    Version: [ {info.VERSION} ]
        """)

        print(console.BLUE("Do 'devgoldy --help' for a list of available commands."))

    else:
        print(console.BLUE(f"Running command {ctx.invoked_subcommand}..."))
        print("")
    
from . import utils
from . import start, usb
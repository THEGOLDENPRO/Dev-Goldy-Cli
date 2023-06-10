import click
from devgoldyutils import Colours
from .. import __version__, dev_goldy_logger

@click.group(invoke_without_command = True)
@click.pass_context
def dev_goldy(ctx: click.Context):
    if ctx.invoked_subcommand is None:
        print(f"""
██████╗░███████╗██╗░░░██╗  ░██████╗░░█████╗░██╗░░░░░██████╗░██╗░░░██╗
██╔══██╗██╔════╝██║░░░██║  ██╔════╝░██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝
██║░░██║█████╗░░╚██╗░██╔╝  ██║░░██╗░██║░░██║██║░░░░░██║░░██║░╚████╔╝░
██║░░██║██╔══╝░░░╚████╔╝░  ██║░░╚██╗██║░░██║██║░░░░░██║░░██║░░╚██╔╝░░
██████╔╝███████╗░░╚██╔╝░░  ╚██████╔╝╚█████╔╝███████╗██████╔╝░░░██║░░░
╚═════╝░╚══════╝░░░╚═╝░░░  ░╚═════╝░░╚════╝░╚══════╝╚═════╝░░░░╚═╝░░░

    Version: [ {__version__} ]
        """)

        print(Colours.BLUE.apply("Do 'devgoldy --help' for a list of available commands."))

    else:
        dev_goldy_logger.info(Colours.BLUE.apply(f"Running command {ctx.invoked_subcommand}..."))
        print("")


# Register sub commands.
# -----------------------
from .commands import *
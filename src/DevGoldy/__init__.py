import click

@click.command()
def devgoldy():
    print("""
██████╗░███████╗██╗░░░██╗  ░██████╗░░█████╗░██╗░░░░░██████╗░██╗░░░██╗
██╔══██╗██╔════╝██║░░░██║  ██╔════╝░██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝
██║░░██║█████╗░░╚██╗░██╔╝  ██║░░██╗░██║░░██║██║░░░░░██║░░██║░╚████╔╝░
██║░░██║██╔══╝░░░╚████╔╝░  ██║░░╚██╗██║░░██║██║░░░░░██║░░██║░░╚██╔╝░░
██████╔╝███████╗░░╚██╔╝░░  ╚██████╔╝╚█████╔╝███████╗██████╔╝░░░██║░░░
╚═════╝░╚══════╝░░░╚═╝░░░  ░╚═════╝░░╚════╝░╚══════╝╚═════╝░░░░╚═╝░░░
    """)

@click.command()
@click.option("-program", "-p", help="Runs program.", required=True)
def start(program):
    pass
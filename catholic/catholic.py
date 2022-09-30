import click

from catholic.commands import register_commands


@click.group
def cli():
    """
    Welcome to catholic-cli!
    """
    pass


register_commands(cli)

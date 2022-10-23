import click

from version import version
from catholic.commands import register_commands
from catholic.core.utils.docs import welcome_text

__version__ = version


@click.group(help=welcome_text())
@click.version_option(__version__)  # will read the version from setup.py
@click.pass_context
def cli(ctx: click.Context):
    """
    Welcome to catholic-cli!
    """
    ctx.obj = "Aseem Savio"
    pass


register_commands(cli)

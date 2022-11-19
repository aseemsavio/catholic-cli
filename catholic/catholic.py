import click

from catholic.commands import register_commands
from catholic.core.utils.docs import welcome_text
from catholic.version import version

__version__ = version


@click.group(help=welcome_text(__version__))
@click.version_option(__version__)
@click.pass_context
def cli(ctx: click.Context):
    """
    Welcome to catholic-cli!
    """
    ctx.obj = "Aseem Savio"
    pass


register_commands(cli)

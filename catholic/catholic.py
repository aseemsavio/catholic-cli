from catholic.commands import register_commands
from catholic.version import version
from typer import Typer

__version__ = version

# This is the root object to which all the commands get registered to.
cli = Typer()

register_commands(cli)

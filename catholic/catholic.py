from catholic.commands import register_commands
from catholic.commands.choice import interactive_cli
from catholic.core.utils.console import display_welcome_text
from catholic.version import version
from typer import Typer, Context

__version__ = version

# This is the root object to which all the commands get registered to.
cli = Typer()


@cli.callback(invoke_without_command=True)
def catholic_features_callback(ctx: Context):
    # Execute this only if there is no sub command.
    # https://typer.tiangolo.com/tutorial/commands/context/#exclusive-executable-callback

    try:
        if ctx.invoked_subcommand is None:
            display_welcome_text()
            interactive_cli()
    except Exception:
        pass


register_commands(cli)

import click

from catholic.commands import register_commands


@click.group(help="Welcome to catholic-cli!")
@click.pass_context
def cli(ctx: click.Context):
    """
    Welcome to catholic-cli!
    """
    ctx.obj = "Aseem Savio"
    pass


register_commands(cli)

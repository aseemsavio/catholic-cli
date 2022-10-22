import click

from catholic.core.missal import execute_missal_command
from catholic.core.utils.docs import paragraph_help


@click.command(help="- Query The Roman Missal")
@click.pass_context
@click.option("--paragraph",
              "--p",
              default=None,
              help=paragraph_help()
              )
@click.option("--search", "--s")
def missal(ctx: click.Context, paragraph, search):
    execute_missal_command(paragraph, search)


@click.command(help="- Alias to query The Roman Missal")
@click.pass_context
@click.option("--paragraph",
              "--p",
              default=None,
              help=paragraph_help()
              )
@click.option("--search", "--s")
def m(ctx: click.Context, paragraph, search):
    execute_missal_command(paragraph, search)

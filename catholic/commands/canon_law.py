import click

from catholic.core.canon import execute
from catholic.core.utils.docs import paragraph_help, search_help


@click.command(help="- Query the Canon Law of The Catholic Church.")
@click.pass_context
@click.option("--paragraph", "--p", default=None, help=paragraph_help())
@click.option("--search", "--s", default=None, help=search_help())
def canon(ctx: click.Context, paragraph, search):
    execute(paragraph, search)


@click.command(help="- Alias to Query the Canon Law of The Catholic Church.")
@click.pass_context
@click.option("--paragraph", "--p", default=None, help=paragraph_help())
@click.option("--search", "--s", default=None, help=search_help())
def cl(ctx: click.Context, paragraph, search):
    execute(paragraph, search)

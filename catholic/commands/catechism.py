import click

from catholic.core.catechism.catechism import execute_catechism_command
from catholic.core.utils.docs import paragraph_help, search_help


@click.command(help="- Query the Catechism of The Catholic Church.")
@click.pass_context
@click.option("--paragraph", "--p", default=None, help=paragraph_help())
@click.option("--search", "--s", help=search_help())
def catechism(ctx: click.Context, paragraph, search):
    execute_catechism_command(paragraph, search)


@click.command(help="- Alias to Query the Catechism of The Catholic Church.")
@click.pass_context
@click.option("--paragraph", "--p", default=None, help=paragraph_help())
@click.option("--search", "--s", help=search_help())
def c(ctx: click.Context, paragraph, search):
    execute_catechism_command(paragraph, search)

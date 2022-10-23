import click

from catholic.core.catechism.api import execute
from catholic.core.utils.docs import paragraph_help_text, search_help_text


@click.command(help="- Query the Catechism of The Catholic Church.")
@click.pass_context
@click.option("--paragraph", "--p", default=None, help=paragraph_help_text())
@click.option("--search", "--s", help=search_help_text())
def catechism(ctx: click.Context, paragraph, search):
    execute(paragraph=paragraph, search=search)


@click.command(help="- Alias to Query the Catechism of The Catholic Church.")
@click.pass_context
@click.option("--paragraph", "--p", default=None, help=paragraph_help_text())
@click.option("--search", "--s", help=search_help_text())
def c(ctx: click.Context, paragraph, search):
    execute(paragraph=paragraph, search=search)

import click

from catholic.core.canon.api import execute
from catholic.core.utils.docs import paragraph_help_text, search_help_text


@click.command(help="- Query the Canon Law of The Catholic Church.")
@click.pass_context
@click.option("--paragraph", "--p", default=None, help=paragraph_help_text())
@click.option("--search", "--s", default=None, help=search_help_text())
def canon(ctx: click.Context, paragraph, search):
    execute(law=paragraph, search=search)

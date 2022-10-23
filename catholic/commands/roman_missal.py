import click

from catholic.core.missal.api import execute
from catholic.core.utils.docs import paragraph_help_text, search_help_text


@click.command(help="- Query The Roman Missal")
@click.pass_context
@click.option("--paragraph", "--p", default=None, help=paragraph_help_text())
@click.option("--search", "--s", help=search_help_text())
def missal(ctx: click.Context, paragraph, search):
    execute(missal_id=paragraph, search=search)


@click.command(help="- Alias to query The Roman Missal")
@click.pass_context
@click.option("--paragraph", "--p", default=None, help=paragraph_help_text())
@click.option("--search", "--s", help=search_help_text())
def m(ctx: click.Context, paragraph, search):
    execute(missal_id=paragraph, search=search)

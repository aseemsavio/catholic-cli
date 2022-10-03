import click

from catholic.core.canon import execute_canon_command


@click.command(help="- Query the Canon Law of The Catholic Church.")
@click.pass_context
@click.option("--paragraph", "--p")
@click.option("--search", "--s")
def canon(ctx: click.Context, paragraph, search):
    execute_canon_command(paragraph, search)


@click.command(help="- Alias to Query the Canon Law of The Catholic Church.")
@click.pass_context
@click.option("--paragraph", "--p")
@click.option("--search", "--s")
def cl(ctx: click.Context, paragraph, search):
    execute_canon_command(paragraph, search)

import click

from catholic.core.canon import execute_canon_command


@click.command(help="- Query the Canon Law of The Catholic Church.")
@click.pass_context
@click.option("--paragraph", "--p", type=int)
def canon(ctx: click.Context, paragraph):
    execute_canon_command(paragraph)


@click.command(help="- Alias to Query the Canon Law of The Catholic Church.")
@click.pass_context
@click.option("--paragraph", "--p", type=int)
def cl(ctx: click.Context, paragraph):
    execute_canon_command(paragraph)

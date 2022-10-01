import click

from catholic.core.canon import execute_canon_command


@click.command(help="- Query the Canon Law of The Catholic Church.")
@click.pass_context
@click.option("--law", "--l", type=int)
def canon(ctx: click.Context, law):
    execute_canon_command(law)


@click.command(help="- Alias to Query the Canon Law of The Catholic Church.")
@click.pass_context
@click.option("--law", "--l", type=int)
def cl(ctx: click.Context, law):
    execute_canon_command(law)

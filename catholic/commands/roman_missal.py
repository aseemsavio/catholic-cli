import click

from catholic.core.missal import execute_missal_command


@click.command()
@click.pass_context
@click.option("--paragraph", "--p")
def missal(ctx: click.Context, paragraph):
    execute_missal_command(paragraph)


@click.command()
@click.pass_context
@click.option("--paragraph", "--p")
def m(ctx: click.Context, paragraph):
    execute_missal_command(paragraph)

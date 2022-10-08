import click

from catholic.core.missal import execute_missal_command


@click.command()
@click.pass_context
@click.option("--paragraph", "--p")
@click.option("--search", "--s")
def missal(ctx: click.Context, paragraph, search):
    execute_missal_command(paragraph, search)


@click.command()
@click.pass_context
@click.option("--paragraph", "--p")
@click.option("--search", "--s")
def m(ctx: click.Context, paragraph, search):
    execute_missal_command(paragraph, search)

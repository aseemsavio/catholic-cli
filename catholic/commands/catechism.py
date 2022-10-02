import click

from catholic.core.catechism.catechism import execute_catechism_command


@click.command(help="- Query the Catechism of The Catholic Church.")
@click.pass_context
@click.option("--paragraph", "--p")
def catechism(ctx: click.Context, paragraph):
    execute_catechism_command(paragraph)


@click.command(help="- Alias to Query the Catechism of The Catholic Church.")
@click.pass_context
@click.option("--paragraph", "--p")
def c(ctx: click.Context, paragraph):
    execute_catechism_command(paragraph)

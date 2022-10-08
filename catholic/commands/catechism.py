import click

from catholic.core.catechism.catechism import execute_catechism_command


@click.command(help="- Query the Catechism of The Catholic Church.")
@click.pass_context
@click.option("--paragraph", "--p")
@click.option("--search", "--s")
def catechism(ctx: click.Context, paragraph, search):
    execute_catechism_command(paragraph, search)


@click.command(help="- Alias to Query the Catechism of The Catholic Church.")
@click.pass_context
@click.option("--paragraph", "--p")
@click.option("--search", "--s")
def c(ctx: click.Context, paragraph, search):
    execute_catechism_command(paragraph, search)

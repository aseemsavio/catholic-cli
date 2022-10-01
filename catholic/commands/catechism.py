import click

from catholic.core.catechism import get_catechism_by_paragraph


@click.command()
@click.pass_context
def catechism(ctx: click.Context):
    print(ctx.obj)
    print(get_catechism_by_paragraph(1))

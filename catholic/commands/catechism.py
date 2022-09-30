import click

from catholic.core.catechism import get_catechism_by_paragraph


@click.command()
def catechism():
    print(get_catechism_by_paragraph(1))

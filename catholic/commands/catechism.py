import click

from catholic.core.catechism import get_catechism_by_paragraph
from catholic.core.utils import load_pickle


@click.command()
@click.pass_context
def catechism(ctx: click.Context):
    catechism_dict = load_pickle("pickles/catechism.pickle")
    print(f"We have {len(catechism_dict)} results for Catechism.")
    print(get_catechism_by_paragraph(1))

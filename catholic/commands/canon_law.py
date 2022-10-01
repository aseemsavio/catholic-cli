import click

from catholic.core.utils import load_pickle


@click.command()
@click.pass_context
def canon(ctx: click.Context):
    canon_law_dict = load_pickle("pickles/canon.pickle")
    print(f"We have {len(canon_law_dict)} results for The Canon Law.")
    print("Canon Law")

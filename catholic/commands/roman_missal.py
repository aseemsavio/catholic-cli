import click

from catholic.core.utils import load_pickle


@click.command()
@click.pass_context
def missal(ctx: click.Context):
    roman_missal = load_pickle("pickles/girm.pickle")
    print(f"We have {len(roman_missal)} results for the Roman Missal")

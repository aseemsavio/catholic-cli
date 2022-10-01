import click

from catholic.core.catechism import get_catechism_by_paragraph
from catholic.core.utils import load_pickle, show_green_block_text, show_error_message, show_markdown


@click.command()
@click.pass_context
@click.option("--paragraph", "--p", type=int)
def catechism(ctx: click.Context, paragraph):
    execute_catechism_command(paragraph)


@click.command()
@click.pass_context
@click.option("--paragraph", "--p", type=int)
def c(ctx: click.Context, paragraph):
    execute_catechism_command(paragraph)


def execute_catechism_command(paragraph):
    catechism_dict = load_pickle("pickles/catechism.pickle")
    if paragraph:
        try:
            catechism_para = get_catechism_by_paragraph(paragraph, catechism_dict)["text"]
            # show_green_block_text(catechism_para)
            show_markdown(catechism_para)
        except IndexError as e:
            error_message = f"🙁 The Catechism does not have a paragraph with ID: {paragraph}"
            show_error_message(error_message)

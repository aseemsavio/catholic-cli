import rich
from rich.console import Console
from rich.markdown import Markdown
from rich.padding import Padding


def show_green_block_text(text: str):
    """
    Shows the given text in green color, and as a block.
    :param text: Text to be shown on the Terminal.
    :return: None
    """
    rich.print(Padding(text, (2, 2, 1, 1), style="green"))


def show_error_message(error_message: str):
    """
    Shows an error message on the console.
    :param error_message: Error message to show
    :return: None
    """
    rich.print(Padding(error_message, (2, 2, 1, 1), style="red"))


def show_markdown(text: str):
    """
    Shows the Markdown on the console.
    :param text: Markdown to show
    :return: None
    """
    console = Console()
    console.line()
    md = Markdown(text, style="green")
    console.print(md)
    console.line()

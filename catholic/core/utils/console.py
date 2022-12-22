import platform

import rich
from rich.align import Align
from rich.console import Console
from rich.markdown import Markdown
from rich.padding import Padding
from rich.panel import Panel

from catholic.version import version


def green_text(text: str):
    """
    Shows the given text in green color, and as a block.
    :param text: Text to be shown on the Terminal.
    :return: None
    """
    rich.print(Padding(text, (1, 1, 1, 1), style="green"))


def blue_boxed_text(text: str):
    """
    Shows the given text in blue, bold color, and as a block.
    :param text: Text to be shown on the Terminal.
    :return: None
    """
    console = Console()
    console.print(Panel(text, title="Gaudete!", title_align="left", highlight=True, border_style="cyan1"))
    console.line()


def red_boxed_text(text: str):
    """
    Shows the given text in red, bold color, and as a block.
    :param text: Text to be shown on the Terminal.
    :return: None
    """
    console = Console()
    console.print(Panel(text, title="Oops!", title_align="left", highlight=True, border_style="red"))
    console.line()


def error(error_message: str):
    """
    Shows an error message on the console.
    :param error_message: Error message to show
    :return: None
    """
    red_boxed_text(error_message)


def markdown(text: str, heading: str = None):
    """
    Shows the Markdown on the console.
    :param heading:
    :param text: Markdown to show
    :return: None
    """

    console = Console()
    if heading:
        console.print(f"    [bold bright_white]{heading}[/bold bright_white]")
    console.print(Padding(Markdown(text, style="gold3", justify="full"), (0, 4, 1, 4)))
    console.line()


def get_platform():
    """
    Gets the OS this app is running on
    :return:
    Linux: Linux
    Mac: Darwin
    Windows: Windows
    """
    return platform.system()


def emoji(emoji_literal, default=""):
    """
    Returns the same emoji if emojis are supported on the current platform. Default text if not.
    :param default: Default string to display in place of the emoji in unsupported OSes.
    :param emoji_literal:
    :return:
    """
    plt = get_platform()
    if plt == "Darwin" or plt == "Linux":
        return emoji_literal
    else:
        return default


def show_matched_para_count(resource: str, matched: list[dict], para: bool = False, search_str: bool = False):
    """
    Displays matched laws count
    :return:
    """

    count = len(matched)

    if para:
        if count == 0:
            error(f"There are no results for the requested paragraph ID(s).")
        elif count == 1:
            blue_boxed_text(f"Showing 1 {resource} paragraph matching ID: {matched[0]['id']}")
        elif count > 1:
            blue_boxed_text(
                f"Showing {count} {resource} paragraphs matching IDs - {[p['id'] for p in matched]}.")
    elif search_str:
        if count == 0:
            error(f"There are no results for the requested search text.")
        elif count == 1:
            blue_boxed_text(f"Showing 1 {resource} paragraph matching the requested search text")
        elif count > 1:
            blue_boxed_text(
                f"Showing {count} {resource} paragraphs matching the requested search text.")


def display_welcome_text():
    c = Console()
    c.line()
    welcome_text = f"\n[bold bright_white]Catholic Command Line Interface[/bold bright_white] - An Awesome Catholic Theological Knowledge Base.\n" \
                   f"                         [dim]Version[/dim]     [gold3]{version}[/gold3]\n" \
                   f"                          [dim]GitHub[/dim]     [gold3]https://github.com/aseemsavio[/gold3]\n"
    c.print(Panel(Align(welcome_text, align="center"),
                  title="Vivo Christo Rey!",
                  subtitle="Sancta Maria, Mater Dei, ora pro nobis!",
                  border_style="gold3", ))
    c.line()

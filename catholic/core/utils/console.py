import platform

import rich
from rich.console import Console
from rich.markdown import Markdown
from rich.padding import Padding


def green_text(text: str):
    """
    Shows the given text in green color, and as a block.
    :param text: Text to be shown on the Terminal.
    :return: None
    """
    rich.print(Padding(text, (1, 1, 1, 1), style="green"))


def blue_text(text: str):
    """
    Shows the given text in blue, bold color, and as a block.
    :param text: Text to be shown on the Terminal.
    :return: None
    """
    rich.print(Padding(text, (1, 0, 0, 4), style="blue bold"))


def red_text(text: str):
    """
    Shows the given text in red, bold color, and as a block.
    :param text: Text to be shown on the Terminal.
    :return: None
    """
    rich.print(Padding(text, (1, 0, 0, 4), style="red bold"))


def error(error_message: str):
    """
    Shows an error message on the console.
    :param error_message: Error message to show
    :return: None
    """
    rich.print(Padding(error_message, (2, 2, 1, 1), style="red"))


def markdown(text: str):
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
            red_text(f"{emoji('❌')} There are no results for the requested paragraph ID(s).")
        elif count == 1:
            blue_text(f"{emoji('✅')} Showing 1 {resource} paragraph matching ID: {matched[0]['id']}")
        elif count > 1:
            blue_text(
                f"{emoji('✅')} Showing {count} {resource} paragraphs matching IDs - {[p['id'] for p in matched]}.")
    elif search_str:
        if count == 0:
            red_text(f"{emoji('❌')} There are no results for the requested search text.")
        elif count == 1:
            blue_text(f"{emoji('✅')} Showing 1 {resource} paragraph matching the requested search text")
        elif count > 1:
            blue_text(
                f"{emoji('✅')} Showing {count} {resource} paragraphs matching the requested search text.")

from typing import Optional

from typer import Typer, Option

from catholic.core.utils.docs import paragraph_help_text, search_help_text

import catholic.core.catechism.api as catechism_api
import catholic.core.canon.api as canon_api
import catholic.core.missal.api as missal_api


def register_commands(cli: Typer):
    """
    This function contains the logic to register the commands in this CLI.
    :param cli: Typer Object to which we register commands
    :return: None
    """

    @cli.command(name="catechism", help="Query The catechism of The Catholic Church.")
    def catechism_impl(paragraph: Optional[str] = Option(None, "--paragraph", "-p", help=paragraph_help_text()),
                       search: Optional[str] = Option(None, "--search", "-s", help=search_help_text())
                       ):
        catechism_api.execute(paragraph=paragraph, search=search)

    @cli.command(name="canon", help="Query The Canon Law of The Catholic Church.")
    def canon_impl(paragraph: Optional[str] = Option(None, "--paragraph", "-p", help=paragraph_help_text()),
                   search: Optional[str] = Option(None, "--search", "-s", help=search_help_text())
                   ):
        canon_api.execute(law=paragraph, search=search)

    @cli.command(name="missal", help="Query The general Instruction of The Roman Missal.")
    def missal_impl(paragraph: Optional[str] = Option(None, "--paragraph", "-p", help=paragraph_help_text()),
                    search: Optional[str] = Option(None, "--search", "-s", help=search_help_text())
                    ):
        missal_api.execute(missal_id=paragraph, search=search)

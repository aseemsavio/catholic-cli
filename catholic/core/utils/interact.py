from typing import Optional

import questionary


def prompt_para_or_search(paragraph: Optional[str],
                          search: Optional[str],
                          search_by: Optional[str],
                          resource_short_name: str,
                          resource_long_name: str
                          ):
    """
    This function prompts para or search.

    :param paragraph:
    :param search:
    :param search_by:
    :param resource_short_name:
    :param resource_long_name:
    :return:
    """

    if paragraph is None and search is None:
        if search_by == "Para":
            paragraph = questionary.text(f"Enter the {resource_short_name} paragraphs you wish to search: ").ask()
        elif search_by == "Text":
            search = questionary.text(f"Enter the exact text you wish to search in {resource_long_name} ").ask()
        else:
            paragraph = questionary.text(f"Enter the {resource_short_name} paragraphs you wish to search: ").ask()
            if not paragraph:
                search = questionary.text(f"Enter the exact text you wish to search in {resource_long_name}: ").ask()

    return paragraph, search

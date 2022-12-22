from dataclasses import dataclass
from enum import Enum
from typing import List

import questionary as q
from catholic.core.canon import api as canon_api
from catholic.core.catechism import api as catechism_api
from catholic.core.missal import api as missal_api


def interactive_cli():
    """
    This function runs the CLI in an interactive mode for non-tech-savy users.
    :return: None
    """

    root = InteractiveCli(
        messages=[
            Resource("catechism", "The Catechism of The Catholic Church", [SearchBy.Para, SearchBy.Text]),
            Resource("canon", "The Canon Law of The Church", [SearchBy.Para, SearchBy.Text]),
            Resource("missal", "The Roman Missal", [SearchBy.Para, SearchBy.Text]),
        ]
    )

    ###
    # root = {
    #     "messages": {
    #         "catechism": "The Catechism of The Catholic Church",
    #         "canon": "The Canon Law of The Church",
    #         "missal": "The Roman Missal"
    #     }
    # }

    # by_para = "Search by Paragraph ID(s)"
    # by_text = "Search by Text"

    resource = q.select(
        "What do you want to search?",
        choices=[r.long_name for r in root.messages]
    ).ask()

    resource_name = [r.short_name for r in root.messages if resource == r.long_name][0]

    search_by = q.select(
        "How do you want to search?",
        choices=[str(v.value) for v in
                 [r for r in root.messages if r.short_name == resource_name][0].search_by_possibilities]
    ).ask()

    para, search_text = None, None

    # if search_by == by_para:
    #     para = q.text(f"Enter the {str(resource_name).capitalize()} paragraphs you wish to search: ").ask()
    # else:
    #     search_text = q.text(f"Enter the exact text you wish to search in {resource}: ").ask()

    if resource_name == "catechism":
        catechism_api.execute(paragraph=None, search=None, search_by=SearchBy(search_by).name)

    elif resource_name == "canon":
        canon_api.execute(law=None, search=None, search_by=SearchBy(search_by).name)

    elif resource_name == "missal":
        missal_api.execute(missal_id=None, search=None, search_by=SearchBy(search_by).name)


class SearchBy(Enum):
    Para = "Search by Paragraph ID(s)"
    Text = "Search by Text"


@dataclass
class Resource:
    short_name: str
    long_name: str
    search_by_possibilities: List[SearchBy]


@dataclass
class InteractiveCli:
    messages: List[Resource]

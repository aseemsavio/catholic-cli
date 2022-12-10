from rich.console import Console

from catholic.core.catechism.services import get_catechism_paragraphs_with_given_substring, \
    get_catechism_paragraphs_by_paragraph_ids, display_catechism_paragraphs, display_catechism_paragraph
from catholic.core.utils.files import load_pickle_by_name
from catholic.core.utils.console import error, show_matched_para_count
from catholic.core.utils.interact import prompt_para_or_search

from catholic.core.utils.query import decode_query


def execute(paragraph, search, search_by: str = None):
    """
    This function is a work-around to achieve command aliasing between "catechism" and "c".
    :param search_by:
    :param search:
    :param paragraph: Paragraph_number
    :return: None
    """

    paragraph, search = prompt_para_or_search(paragraph,
                                              search,
                                              search_by,
                                              "Catechism",
                                              "The Catechism of The Catholic Church")

    catechism_dict = load_pickle_by_name("catechism.pickle")
    Console().line()

    # --p or --paragraph is found in the command
    if paragraph:

        # Example: --p 101
        if paragraph.isdigit():
            display_catechism_paragraph(catechism_dict, paragraph)

        # Example: --p "1,2,5-8"
        else:
            try:
                paragraph_ids = decode_query(paragraph)
                matched_paragraphs = get_catechism_paragraphs_by_paragraph_ids(paragraph_ids, catechism_dict)
                display_catechism_paragraphs(matched_paragraphs)
                show_matched_para_count(resource="Catechism", matched=matched_paragraphs, para=True)
            except Exception:
                error(f"Could not decode the query: {paragraph}")

    # --s or --search is found in the command
    elif search:
        try:
            matched_catechism_paragraphs = get_catechism_paragraphs_with_given_substring(search, catechism_dict)
            display_catechism_paragraphs(matched_catechism_paragraphs)
            show_matched_para_count(resource="Catechism", matched=matched_catechism_paragraphs, search_str=True)
        except Exception:
            error(f"Could not decode the search string: {search}")

from rich.console import Console

from catholic.core.missal.services import \
    get_roman_missal_paragraphs_with_given_substring, \
    get_roman_missal_paragraphs_by_numbers, \
    display_missal_paragraph, \
    display_missal_paragraphs
from catholic.core.utils.files import load_pickle_by_name
from catholic.core.utils.console import error, show_matched_para_count
from catholic.core.utils.interact import prompt_para_or_search
from catholic.core.utils.query import decode_query


def execute(missal_id, search, search_by: str = None):
    missal_id, search = prompt_para_or_search(missal_id,
                                              search,
                                              search_by,
                                              "Missal",
                                              "The Roman Missal")

    missal_dict = load_pickle_by_name("girm.pickle")
    Console().line()

    # --p or --paragraph is found in the command
    if missal_id:

        # Example: --p 101
        if missal_id.isdigit():
            display_missal_paragraph(missal_dict, missal_id)

        # Example: --p "1,2,5-8"
        else:
            try:
                missal_ids = decode_query(missal_id)
                matched_paragraphs = get_roman_missal_paragraphs_by_numbers(missal_ids, missal_dict)
                display_missal_paragraphs(matched_paragraphs)
                show_matched_para_count(resource="Roman Missal", matched=matched_paragraphs, para=True)
            except Exception:
                error(f"Could not decode the query: {missal_id}")

    # --s or --search is found in the command
    elif search:
        try:
            matched_missal_paragraphs = get_roman_missal_paragraphs_with_given_substring(search, missal_dict)
            display_missal_paragraphs(matched_missal_paragraphs)
            show_matched_para_count(resource="Roman Missal", matched=matched_missal_paragraphs, search_str=True)
        except Exception:
            error(f"Could not decode the search string: {search}")

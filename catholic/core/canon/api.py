from rich.console import Console

from catholic.core.canon.services import get_canon_laws_with_given_substring, \
    get_canon_law_paragraphs_by_paragraph_ids, display_canon_law, display_canon_laws
from catholic.core.utils.files import load_pickle_by_name
from catholic.core.utils.console import error, show_matched_para_count
from catholic.core.utils.interact import prompt_para_or_search
from catholic.core.utils.query import decode_query


def execute(law, search, search_by: str = None):
    law, search = prompt_para_or_search(law,
                                        search,
                                        search_by,
                                        "Canon",
                                        "The Canon Law")

    canon_law_dict = load_pickle_by_name("canon.pickle")
    Console().line()

    # --p or --paragraph is found in the command
    if law:
        # Example: --p 101
        if law.isdigit():
            display_canon_law(canon_law_dict, law)

        # Example: --p "1,2,5-8"
        else:
            try:
                law_ids = decode_query(law)
                matched_laws: list[dict] = get_canon_law_paragraphs_by_paragraph_ids(law_ids, canon_law_dict)
                display_canon_laws(matched_laws)
                show_matched_para_count(resource="Canon Law", matched=matched_laws, para=True)
            except Exception:
                error(f"Could not decode the query: {law}")
    # --s or --search is found in the command
    elif search:
        try:
            matched_laws = get_canon_laws_with_given_substring(search, canon_law_dict)
            display_canon_laws(matched_laws)
            show_matched_para_count(resource="Canon Law", matched=matched_laws, search_str=True)
        except Exception:
            error(f"Could not decode the search string: {search}")

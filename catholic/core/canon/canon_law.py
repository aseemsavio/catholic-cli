from catholic.core.canon.services import get_canon_law_by_id
from catholic.core.utils import load_pickle, show_error_message, show_markdown, show_blue_bold_block_text
from catholic.core.utils.query import decode_query


def execute_canon_command(law):
    canon_law_dict = load_pickle("pickles/canon.pickle")
    if law.isdigit():
        _display_canon_law(canon_law_dict, law)
    else:
        try:
            for individual_law in decode_query(law):
                _display_canon_law(canon_law_dict, individual_law)
        except ValueError:
            error_message = f"🙁 Could not decode the query: {law}"
            show_error_message(error_message)


def _display_canon_law(canon_law_dict, law):
    try:
        canon_law = get_canon_law_by_id(int(law), canon_law_dict)
        if "text" in canon_law:
            show_blue_bold_block_text(f"Canon Law: {canon_law['id']}")
            show_markdown(canon_law["text"])
        elif "sections" in canon_law:
            for section in canon_law["sections"]:
                show_blue_bold_block_text(f"Canon Law: {canon_law['id']} :: §{section['id']}")
                show_markdown(section["text"])
    except IndexError:
        error_message = f"🙁 There is no Canon Law with ID: {law}"
        show_error_message(error_message)

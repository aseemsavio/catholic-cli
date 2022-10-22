from catholic.core.canon.services import get_canon_law_by_id, get_canon_laws_with_given_substring, \
    get_canon_law_paragraphs_by_paragraph_ids
from catholic.core.utils.files import load_pickle_by_name
from catholic.core.utils.console import error, markdown, blue_text, red_text
from catholic.core.utils.query import decode_query


def execute_canon_command(law, search):
    canon_law_dict = load_pickle_by_name("canon.pickle")
    if law:
        if law.isdigit():
            _display_canon_law(canon_law_dict, law)
        else:
            try:
                law_ids = decode_query(law)
                matched_laws: list[dict] = get_canon_law_paragraphs_by_paragraph_ids(law_ids, canon_law_dict)
                _display_canon_laws(matched_laws)
                if len(matched_laws) > 0:
                    blue_text(
                        f"✅ Showing {len(matched_laws)} Canon Law(s) matching Law ID(s) "
                        f"- {[p['id'] for p in matched_laws]}.")
                else:
                    red_text(
                        f"❌ Showing {len(matched_laws)} Canon Law(s) matching Law IDs "
                        f"- {[p['id'] for p in matched_laws]}.")
            except ValueError:
                error_message = f"🙁 Could not decode the query: {law}"
                error(error_message)
    elif search:
        try:
            matched_laws = get_canon_laws_with_given_substring(search, canon_law_dict)
            _display_canon_laws(matched_laws)
            if len(matched_laws) > 0:
                blue_text(
                    f"✅ Showing {len(matched_laws)} Canon Law(s) matching the substring - `{search}`.")
            else:
                red_text(
                    f"❌ Showing {len(matched_laws)} Canon Laws matching the substring - `{search}`.")
        except ValueError:
            error_message = f"🙁 Could not decode the search string: {search}"
            error(error_message)


def _display_canon_law(canon_law_dict, law):
    try:
        canon_law = get_canon_law_by_id(int(law), canon_law_dict)
        if "text" in canon_law:
            blue_text(f"Canon Law: {canon_law['id']}")
            markdown(canon_law["text"])
        elif "sections" in canon_law:
            for section in canon_law["sections"]:
                blue_text(f"Canon Law: {canon_law['id']} :: §{section['id']}")
                markdown(section["text"])
    except IndexError:
        error_message = f"🙁 There is no Canon Law with ID: {law}"
        error(error_message)


def _display_canon_laws(canon_law_dict: list[dict]):
    """

    :param canon_law_dict:
    :return:
    """
    for canon_law in canon_law_dict:
        if "text" in canon_law:
            blue_text(f"Canon Law: {canon_law['id']}")
            markdown(canon_law["text"])
        elif "sections" in canon_law:
            for section in canon_law["sections"]:
                blue_text(f"Canon Law: {canon_law['id']} :: §{section['id']}")
                markdown(section["text"])

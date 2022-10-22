from catholic.core.catechism.services import get_catechism_by_paragraph, \
    get_catechism_paragraphs_with_given_substring, get_catechism_paragraphs_by_paragraph_ids
from catholic.core.utils.files import load_pickle
from catholic.core.utils.console import markdown, error, blue_text, red_text

from catholic.core.utils.query import decode_query


def execute_catechism_command(paragraph, search):
    """
    This function is a work-around to achieve command aliasing between "catechism" and "c".
    :param search:
    :param paragraph: Paragraph_number
    :return: None
    """
    catechism_dict = load_pickle("pickles/catechism.pickle")
    if paragraph:
        if paragraph.isdigit():
            _display_catechism_paragraph(catechism_dict, paragraph)
        else:
            try:
                paragraph_ids = decode_query(paragraph)
                matched_paragraphs = get_catechism_paragraphs_by_paragraph_ids(paragraph_ids, catechism_dict)
                _display_catechism_paragraphs(matched_paragraphs)
                if len(matched_paragraphs) > 0:
                    blue_text(
                        f"✅ Showing {len(matched_paragraphs)} Catechism paragraph(s) matching paragraph ID(s) "
                        f"- {[p['id'] for p in matched_paragraphs]}.")
                else:
                    red_text(
                        f"❌ Showing {len(matched_paragraphs)} Catechism paragraphs matching paragraph IDs "
                        f"- {[p['id'] for p in matched_paragraphs]}.")
            except ValueError:
                error_message = f"🙁 Could not decode the query: {paragraph}"
                error(error_message)
    elif search:
        try:
            matched_catechism_paragraphs = get_catechism_paragraphs_with_given_substring(search, catechism_dict)
            _display_catechism_paragraphs(matched_catechism_paragraphs)
            if len(matched_catechism_paragraphs) > 0:
                blue_text(
                    f"✅ Showing {len(matched_catechism_paragraphs)} Catechism paragraph(s) matching substring "
                    f"-`{search}`.")
            else:
                red_text(
                    f"❌ Showing {len(matched_catechism_paragraphs)} Catechism paragraphs matching substring "
                    f"-`{search}`.")
        except ValueError:
            error_message = f"🙁 Could not decode the search string: {search}"
            error(error_message)


def _display_catechism_paragraph(catechism_dict, paragraph):
    try:
        catechism_para = get_catechism_by_paragraph(int(paragraph), catechism_dict)
        blue_text(f"Catechism Paragraph: {catechism_para['id']}")
        markdown(catechism_para["text"])
    except IndexError:
        error_message = f"🙁 The Catechism does not have a paragraph with ID: {paragraph}"
        error(error_message)


def _display_catechism_paragraphs(paragraphs: list[dict]):
    """

    :param paragraphs:
    :return:
    """
    for paragraph in paragraphs:
        blue_text(f"Catechism Paragraph: {paragraph['id']}")
        markdown(paragraph["text"])

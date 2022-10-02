from catholic.core.catechism.services import get_catechism_by_paragraph
from catholic.core.utils import load_pickle, show_markdown, show_error_message, show_blue_bold_block_text
from catholic.core.utils.query import decode_query


def execute_catechism_command(paragraph):
    """
    This function is a work-around to achieve command aliasing between "catechism" and "c".
    :param paragraph: Paragraph_number
    :return: None
    """
    catechism_dict = load_pickle("pickles/catechism.pickle")
    if paragraph.isdigit():
        _display_catechism_paragraph(catechism_dict, paragraph)
    else:
        try:
            for individual_para in decode_query(paragraph):
                _display_catechism_paragraph(catechism_dict, individual_para)
        except ValueError:
            error_message = f"🙁 Could not decode the query: {paragraph}"
            show_error_message(error_message)


def _display_catechism_paragraph(catechism_dict, paragraph):
    try:
        catechism_para = get_catechism_by_paragraph(int(paragraph), catechism_dict)
        show_blue_bold_block_text(f"Catechism Paragraph: {catechism_para['id']}")
        show_markdown(catechism_para["text"])
    except IndexError:
        error_message = f"🙁 The Catechism does not have a paragraph with ID: {paragraph}"
        show_error_message(error_message)

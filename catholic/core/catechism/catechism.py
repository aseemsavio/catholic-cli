from catholic.core.catechism.services import get_catechism_by_paragraph
from catholic.core.utils import load_pickle, show_markdown, show_error_message


def execute_catechism_command(paragraph):
    """
    This function is a work-around to achieve command aliasing between "catechism" and "c".
    :param paragraph: Paragraph_number
    :return: None
    """
    catechism_dict = load_pickle("pickles/catechism.pickle")
    if paragraph:
        try:
            catechism_para = get_catechism_by_paragraph(paragraph, catechism_dict)["text"]
            show_markdown(catechism_para)
        except IndexError:
            error_message = f"🙁 The Catechism does not have a paragraph with ID: {paragraph}"
            show_error_message(error_message)

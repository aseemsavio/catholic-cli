from catholic.core.missal.services import get_roman_missal_by_number
from catholic.core.utils import load_pickle, show_markdown, show_error_message, show_blue_bold_block_text
from catholic.core.utils.query import decode_query


def execute_missal_command(missal_id):
    missal_dict = load_pickle("pickles/girm.pickle")
    if missal_id.isdigit():
        _display_missal_paragraph(missal_dict, missal_id)
    else:
        try:
            for individual_missal in decode_query(missal_id):
                _display_missal_paragraph(missal_dict, individual_missal)
        except ValueError:
            error_message = f"🙁 Could not decode the query: {missal_id}"
            show_error_message(error_message)


def _display_missal_paragraph(missal_dict, missal_id):
    try:
        missal_para = get_roman_missal_by_number(int(missal_id), missal_dict)
        show_blue_bold_block_text(f"General Instruction of The Roman Missal - Paragraph: {missal_para['id']}")
        show_markdown(missal_para["text"])
    except IndexError:
        error_message = f"🙁 The Missal does not have a section with ID: {missal_id}"
        show_error_message(error_message)

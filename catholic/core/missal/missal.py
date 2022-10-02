from catholic.core.missal.services import get_roman_missal_by_number
from catholic.core.utils import load_pickle, show_markdown, show_error_message, show_blue_bold_block_text


def execute_missal_command(missal_id):
    missal_dict = load_pickle("pickles/girm.pickle")
    if missal_id.isdigit():
        try:
            missal_para = get_roman_missal_by_number(int(missal_id), missal_dict)
            show_blue_bold_block_text(f"General Instruction of The Roman Missal - Paragraph: {missal_para['id']}")
            show_markdown(missal_para["text"])
        except IndexError:
            error_message = f"🙁 The Missal does not have a section with ID: {missal_id}"
            show_error_message(error_message)
    else:
        print(missal_id)

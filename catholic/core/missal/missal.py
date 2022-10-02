from catholic.core.missal.services import get_roman_missal_by_number
from catholic.core.utils import load_pickle, show_markdown, show_error_message


def execute_missal_command(missal_id):
    missal_dict = load_pickle("pickles/girm.pickle")
    if missal_id:
        try:
            missal_para = get_roman_missal_by_number(missal_id, missal_dict)["text"]
            show_markdown(missal_para)
        except IndexError:
            error_message = f"🙁 The Missal does not have a section with ID: {missal_id}"
            show_error_message(error_message)

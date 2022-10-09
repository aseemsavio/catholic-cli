from catholic.core.missal.services import get_roman_missal_by_number, get_roman_missal_paragraphs_with_given_substring, \
    get_roman_missal_paragraphs_by_numbers
from catholic.core.utils import load_pickle, show_markdown, show_error_message, show_blue_bold_block_text, \
    show_red_bold_block_text
from catholic.core.utils.query import decode_query


def execute_missal_command(missal_id, search):
    missal_dict = load_pickle("pickles/girm.pickle")
    if missal_id:
        if missal_id.isdigit():
            _display_missal_paragraph(missal_dict, missal_id)
        else:
            try:
                missal_ids = decode_query(missal_id)
                matched_paragraphs = get_roman_missal_paragraphs_by_numbers(missal_ids, missal_dict)
                _display_missal_paragraphs(matched_paragraphs)
                if len(matched_paragraphs) > 0:
                    show_blue_bold_block_text(
                        f"✅ Showing {len(matched_paragraphs)} Missal paragraph(s) matching paragraph ID(s) "
                        f"- {[p['id'] for p in matched_paragraphs]}.")
                else:
                    show_red_bold_block_text(
                        f"❌ Showing {len(matched_paragraphs)} Missal paragraphs matching paragraph IDs "
                        f"- {[p['id'] for p in matched_paragraphs]}.")
            except ValueError:
                error_message = f"🙁 Could not decode the query: {missal_id}"
                show_error_message(error_message)
    elif search:
        matched_missal_paragraphs = get_roman_missal_paragraphs_with_given_substring(search, missal_dict)
        missal_ids = decode_query(missal_id)
        matched_paragraphs = get_roman_missal_paragraphs_by_numbers(missal_ids, missal_dict)
        _display_missal_paragraphs(matched_paragraphs)
        if len(matched_missal_paragraphs) > 0:
            show_blue_bold_block_text(
                f"✅ Showing {len(matched_missal_paragraphs)} Missal paragraph(s) matching substring - `{search}`")
        else:
            show_red_bold_block_text(
                f"❌ Showing {len(matched_missal_paragraphs)} Missal paragraphs matching substring - `{search}`")


def _display_missal_paragraph(missal_dict, missal_id):
    try:
        missal_para = get_roman_missal_by_number(int(missal_id), missal_dict)
        show_blue_bold_block_text(f"General Instruction of The Roman Missal - Paragraph: {missal_para['id']}")
        show_markdown(missal_para["text"])
    except IndexError:
        error_message = f"🙁 The Missal does not have a section with ID: {missal_id}"
        show_error_message(error_message)


def _display_missal_paragraphs(paragraphs: list[dict]):
    """

    :param paragraphs:
    :return:
    """
    for paragraph in paragraphs:
        show_blue_bold_block_text(f"General Instruction of The Roman Missal - Paragraph: {paragraph['id']}")
        show_markdown(paragraph["text"])

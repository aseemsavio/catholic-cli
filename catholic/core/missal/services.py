from catholic.core.utils.console import markdown, error
from catholic.core.utils.strings import string_contains


def get_roman_missal_by_number(missal_id: int, missal: list[dict]):
    """
    Returns the Missal contents in mark down format.
    :param missal_id:
    :param missal:
    :return: Markdown string containing the contents of The Roman Missal.
    """
    return [para for para in missal if para["id"] == missal_id][0]


def get_roman_missal_paragraphs_by_numbers(missal_ids: list[int], missal: list[dict]):
    """

    :param missal_ids:
    :param missal:
    :return:
    """
    return [para for para in missal if para["id"] in missal_ids]


def get_roman_missal_paragraphs_with_given_substring(substring: str, missal: list[dict]) -> list[dict]:
    """

    :param substring:
    :param missal:
    :return:
    """
    return [para for para in missal if string_contains(substring, para["text"])]


def display_missal_paragraph(missal_dict, missal_id):
    try:
        paragraph = get_roman_missal_by_number(int(missal_id), missal_dict)
        display_paragraph(paragraph)
    except IndexError:
        error(f"The Missal does not have a section with ID: {missal_id}")


def display_missal_paragraphs(paragraphs: list[dict]):
    """

    :param paragraphs:
    :return:
    """
    for paragraph in paragraphs:
        display_paragraph(paragraph)


def display_paragraph(paragraph):
    markdown(text=paragraph["text"], heading=f"General Instruction of The Roman Missal - Paragraph: {paragraph['id']}")

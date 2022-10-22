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


def get_roman_missal_paragraphs_with_given_substring(substring: str, missal: list[dict]) -> list[int]:
    """

    :param substring:
    :param missal:
    :return:
    """
    return [para["id"] for para in missal if string_contains(substring, para["text"])]

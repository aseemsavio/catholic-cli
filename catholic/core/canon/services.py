from catholic.core.utils.console import markdown, error
from catholic.core.utils.strings import string_contains


def get_canon_law_by_id(law_id: int, canon: list[dict]):
    """
        Returns the contents of the Canon Law .
        :param canon: Dictionary containing The Canon Law of The Catholic Church.
        :param law_id: Law ID
        :return: String containing the contents of the paragraph.
        """
    return [law for law in canon if law["id"] == law_id][0]


def get_canon_law_paragraphs_by_paragraph_ids(paragraph_ids: list[int], canon: list[dict]):
    """
    Returns all the Canon Law Paragraphs in the given ID list.
    :param paragraph_ids:
    :param canon:
    :return:
    """
    return [paragraph for paragraph in canon if paragraph["id"] in paragraph_ids]


def get_canon_laws_with_given_substring(substring: str, canon: list[dict]) -> list[dict]:
    """

    :param substring:
    :param canon:
    :return:
    """
    matching_canon_laws = []
    for law in canon:
        if "text" in law:
            if string_contains(substring, law["text"]):
                matching_canon_laws.append(law)
        elif "sections" in law:
            for section in law["sections"]:
                if string_contains(substring, section["text"]):
                    matching_canon_laws.append(law)
                    break
    return matching_canon_laws


def display_laws_and_sub_laws(canon_law):
    if "text" in canon_law:
        markdown(text=canon_law["text"], heading=f"Canon Law: {canon_law['id']}")
    elif "sections" in canon_law:
        for section in canon_law["sections"]:
            markdown(text=section["text"], heading=f"Canon Law: {canon_law['id']} :: §{section['id']}")


def display_canon_law(canon_law_dict, law):
    try:
        canon_law = get_canon_law_by_id(int(law), canon_law_dict)
        display_laws_and_sub_laws(canon_law)
    except IndexError:
        error(f"There is no Canon Law with ID: {law}")


def display_canon_laws(canon_law_dict: list[dict]):
    """

    :param canon_law_dict:
    :return:
    """
    for canon_law in canon_law_dict:
        display_laws_and_sub_laws(canon_law)

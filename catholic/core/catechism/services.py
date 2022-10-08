from catholic.core.utils import string_contains


def get_catechism_by_paragraph(paragraph_number: int, catechism: list[dict]):
    """
    Returns the contents of the paragraph in mark down format.
    :param catechism: Dictionary containing The Catechism of The Catholic Church.
    :param paragraph_number: Paragraph Number
    :return: Markdown String containing the contents of the paragraph.
    """
    return [para for para in catechism if para["id"] == paragraph_number][0]


def get_catechism_paragraphs_with_given_substring(substring: str, catechism: list[dict]) -> list[int]:
    """

    :param substring:
    :param catechism:
    :return:
    """
    matching_catechism_laws = []
    for para in catechism:
        if string_contains(substring, para["text"]):
            matching_catechism_laws.append(para["id"])
    return matching_catechism_laws

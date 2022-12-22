from catholic.core.utils.console import markdown, error
from catholic.core.utils.strings import string_contains


def get_catechism_by_paragraph(paragraph_number: int, catechism: list[dict]):
    """
    Returns the contents of the paragraph in mark down format.
    :param catechism: Dictionary containing The Catechism of The Catholic Church.
    :param paragraph_number: Paragraph Number
    :return: Markdown String containing the contents of the paragraph.
    """
    return [para for para in catechism if para["id"] == paragraph_number][0]


def get_catechism_paragraphs_by_paragraph_ids(paragraph_ids: list[int], catechism: list[dict]):
    """
    Returns all the Catechism Paragraphs in the given ID list.
    :param paragraph_ids:
    :param catechism:
    :return:
    """
    return [paragraph for paragraph in catechism if paragraph["id"] in paragraph_ids]


def get_catechism_paragraphs_with_given_substring(substring: str, catechism: list[dict]) -> list[dict]:
    """

    :param substring:
    :param catechism:
    :return:
    """
    return [para for para in catechism if string_contains(substring, para["text"])]


def display_catechism_paragraph(catechism_dict, paragraph):
    try:
        paragraph = get_catechism_by_paragraph(int(paragraph), catechism_dict)
        markdown(text=paragraph["text"], heading=f"Catechism Paragraph: {paragraph['id']}")
    except IndexError:
        error(f"The Catechism does not have a paragraph with ID: {paragraph}")


def display_catechism_paragraphs(paragraphs: list[dict]):
    """

    :param paragraphs:
    :return:
    """
    for paragraph in paragraphs:
        display_paragraph(paragraph)


def display_paragraph(paragraph):
    markdown(text=paragraph["text"], heading=f"Catechism Paragraph: {paragraph['id']}")

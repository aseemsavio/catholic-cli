def get_catechism_by_paragraph(paragraph_number: int, catechism: dict):
    """
    Returns the contents of the paragraph in mark down format.
    :param catechism: Dictionary containing The Catechism of The catholic Church.
    :param paragraph_number: Paragraph Number
    :return: Markdown String containing the contents of the paragraph.
    """
    return [para for para in catechism if para["id"] == paragraph_number][0]
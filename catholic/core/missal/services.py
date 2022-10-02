def get_roman_missal_by_number(missal_id: int, missal: list[dict]):
    """
    Returns the Missal contents in mark down format.
    :param missal_id:
    :param missal:
    :return: Markdown string containing the contents of The Roman Missal.
    """
    return [para for para in missal if para["id"] == missal_id][0]

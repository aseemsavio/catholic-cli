from catholic.core.utils import string_contains


def get_canon_law_by_id(law_id: int, canon: list[dict]):
    """
        Returns the contents of the Canon Law .
        :param canon: Dictionary containing The Canon Law of The Catholic Church.
        :param law_id: Law ID
        :return: String containing the contents of the paragraph.
        """
    return [law for law in canon if law["id"] == law_id][0]


def get_canon_laws_with_given_substring(substring: str, canon: list[dict]) -> list[int]:
    """

    :param substring:
    :param canon:
    :return:
    """
    matching_canon_laws = []
    for law in canon:
        if "text" in law:
            if string_contains(substring, law["text"]):
                matching_canon_laws.append(law["id"])
        elif "sections" in law:
            for section in law["sections"]:
                if string_contains(substring, section["text"]):
                    matching_canon_laws.append(law["id"])
                    break
    return matching_canon_laws

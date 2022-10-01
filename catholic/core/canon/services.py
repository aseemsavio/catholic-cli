def get_canon_law_by_id(law_id: int, canon: dict):
    """
        Returns the contents of the Canon Law .
        :param canon: Dictionary containing The Canon Law of The Catholic Church.
        :param law_id: Law ID
        :return: String containing the contents of the paragraph.
        """
    return [law for law in canon if law["id"] == law_id][0]

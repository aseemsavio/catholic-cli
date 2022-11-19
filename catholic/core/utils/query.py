from catholic.core.utils.strings import remove_white_spaces, destructure_comma_separated_string, \
    range_or_single_digit_list, get_uniques_as_sorted_list


def decode_query(query: str) -> list[int]:
    """
    Decodes the query string into a list of integers.
    Example queries:

    Input       Explanation                 Output

    1,2,3       comma separated             [1, 2, 3]
    1-3         x to y                      [1, 2, 3]
    1,2,3-5     combination of the above    [1, 2, 3, 4, 5]

    :param query: query string
    :return: list of ints.
    """
    # first we remove the excess white spaces from the query
    query_string = remove_white_spaces(query)

    # Now, we destructure the string into the list by comma
    query_list = destructure_comma_separated_string(query_string)

    final_query_list = []
    for query_item in query_list:
        query_sub_list = range_or_single_digit_list(query_item)
        final_query_list.extend(query_sub_list)

    return get_uniques_as_sorted_list(final_query_list)

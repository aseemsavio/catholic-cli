"""
Example queries:

1,2,3       comma separated
1-3         x to y
1,2,3-5     combination of the above
"""


def remove_white_spaces(text: str) -> str:
    """
    Removes white spaces and returns a new string without white spaces.
    :param text:
    :return:
    """
    return "".join(text.split())


def destruct_comma_separated_string(comma_separated_string) -> list[str]:
    """
    Destructs the given string with commas into a list of strings.
    :param comma_separated_string:
    :return:
    """
    return comma_separated_string.split(",")


def range_or_single_digit_list(text: str) -> list:
    """
    if 1, return [1]
    if 1-4, return [1, 2, 3, 4]
    :param text:
    :return:
    """
    if text.isdigit():
        return [int(text)]
    else:
        return range_string_to_int_list(text)


def range_string_to_int_list(range_string: str) -> list[int]:
    """

    :param range_string:
    :return:
    """
    start, end = range_string.split("-")
    return [*range(int(start), int(end) + 1)]


def get_uniques_as_list(list_with_duplicates: list[int]) -> list[int]:
    """

    :param list_with_duplicates:
    :return:
    """
    return list(set(list_with_duplicates))


print(range_or_single_digit_list("1"))
print(range_or_single_digit_list("1-5"))

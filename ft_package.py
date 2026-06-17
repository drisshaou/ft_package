# ./ft_package.py


def count_in_list(lst: list, value) -> int:
    """
    Count the occurrences of a value in a list.
    """
    count = 0
    for elem in lst:
        if elem == value:
            count += 1
    return count

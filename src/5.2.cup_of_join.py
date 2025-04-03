def cup_of_join(*lists, sep=None):
    """Join lists with separator after EVERY list (including last and empty ones).
    Args:
        *lists: Lists to join
        sep: Separator to insert after each list (if provided)
    Returns:
        New list with elements joined by separators
    """
    result = []
    for lst in lists:
        result.extend(lst)
        if sep is not None:  # Critical: check sep here, not outside loop
            result.append(sep)
    return result

if __name__ == '__main__':
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep="@"))  # Output: [1, 2, '@', 8, '@', 9, 5, 6, '@']
    print(cup_of_join([1, 2], [8], [9, 5, 6]))           # Output: [1, 2, 8, 9, 5, 6]
    print(cup_of_join([1]))                               # Output: [1]
    print(cup_of_join())                                   # Output: []
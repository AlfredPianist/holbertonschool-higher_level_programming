#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a roman number (https://en.wikipedia.org/wiki/Roman_numerals)
    to an integer.

    Parameters
    ----------
    roman_string : str
        The roman number to be converted.

    Returns
    -------
    int
        The converted roman number, or 0 if roman_string not a string or None.

    """
    num, i = 0, 0
    r_nums = {
        'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1
    }

    if type(roman_string) != str or roman_string is None:
        return num

    while i < len(roman_string):
        if i + 1 < len(roman_string) and \
           r_nums[roman_string[i]] < r_nums[roman_string[i + 1]]:
            num += r_nums[roman_string[i + 1]] - r_nums[roman_string[i]]
            i += 2
        else:
            num += r_nums[roman_string[i]]
            i += 1

    return num

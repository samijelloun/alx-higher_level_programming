#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    Convert a Roman numeral to an integer.

    Args:
        roman_string (str): The Roman numeral string.

    Returns:
        int: The corresponding integer value or 0 if invalid input.
    """
    if not roman_string or not isinstance(roman_string, str):
        return 0

    total = 0
    digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    for roman in reversed(roman_string):
        arabic = digits.get(roman, 0)
        total += arabic if total < arabic * 5 else -arabic

    return total

"""
Documenting Code Example 1

Author:   Adrian Gould
Date:     2025-03-28
"""

def higher_or_lower(guess_number, target_number):
    """
    Determines if the guess is higher or lower than
    the target number.

    Parameters
    ----------
    guess_number : an integer number
    target_number : an integer humber

    Returns
    -------
    result : string
    A string with "H" for higher, "L" for Lower

    Examples
    --------
    >>> higher_or_lower(0, 1)
    'L'
    >>> higher_or_lower(1, 0)
    'H'
    >>> higher_or_lower(0, 0)
    'E'
    >>> higher_or_lower(-1, 1)
    'L'
    """
    if guess_number < target_number:
        return "L"
    if guess_number > target_number:
        return "H"
    return "E"


import doctest

doctest.testmod()

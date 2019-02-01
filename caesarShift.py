from letnum import ltn, ntl
def caesar(text, shift):
    """
    Description:
    A cipher that shifts each letter by n positions.

    Equation:
    (letter + shift) % 26

    Test Cases:
    >>> caesar("abcdefghijklmnopqrstuvwxyz", 1)
    'bcdefghijklmnopqrstuvwxyza'
    >>> caesar("abcdefghijklmnopqrstuvwxyz", 25)
    'zabcdefghijklmnopqrstuvwxy'
    >>> caesar("abcdefghijklmnopqrstuvwxyz", 13)
    'nopqrstuvwxyzabcdefghijklm'
    """
    assert 0 < shift < 26, "Shift must be between 1 and 25!"
    nums = []
    for x in ltn(text):
        if type(x) == int:
            nums.append((x + shift) % 26)
        else:
            nums.append(x)
    return ntl(nums)

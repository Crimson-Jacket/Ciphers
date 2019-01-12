from letnum import ltn, ntl
def caesar(text, shift):
    """
    Shifts each letter in text by n positions.
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
            if x == " ":
                nums.append(" ")
            else:
                nums.append(x)
    return ntl(nums)
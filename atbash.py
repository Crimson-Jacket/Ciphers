from letnum import ltn, ntl
def atbash(text):
    """
    Replace each letter in text with its opposite letter (abs(letter_position - 25))
    >>> atbash("abcdefghijklmnopqrstuvwxyz")
    'zyxwvutsrqponmlkjihgfedcba'
    """
    nums = []
    for x in ltn(text):
        if type(x) == int:
            nums.append(abs(x - 25))
        else:
            nums.append(x)
    return ntl(nums)
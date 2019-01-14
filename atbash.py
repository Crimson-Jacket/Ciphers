from letnum import ltn, ntl
def atbash(text):
    """
    Description:
    Replaces each letter in text with its "opposite" letter 
    
    General Equation:
    (abs(letter_position - 25))

    Doctests:
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
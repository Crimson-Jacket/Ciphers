def ltn(text):
    """
    Converts letters in text into numbers. Used in other ciphers.
    """
    return [ord(x) - 97 if 97 <= ord(x) <= 122 else x for x in text.lower()]

def ltnKey(text):
    """
    Converts letters in text into numbers. Gets rid of all non-alphabetic symbols.
    """
    return [ord(x) - 97 for x in text.lower() if 97 <= ord(x) <= 122]

def ntl(nums):
    """
    Converts valid numbers into letters.
    >>> ntl([20, 8, 9, 19, '.', ' ', 9, '3', 19, ' ', 1, ' ', 20, 5, '2', 19, 20])
    'uijt. j3t b uf2tu'
    """
    text = ""
    for x in nums:
        if type(x) == int and -1 < x < 26:
            text += str(chr(x + 97))
        else:
            text += str(x)
    return text
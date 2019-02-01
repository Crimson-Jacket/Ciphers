def ltn(text):
    """
    Description:
    Converts letters into numbers.

    Program Notes:
    Abstraction for other ciphers. 
    Return type is an array for convenience.
    """
    return [ord(x) - 97 if 97 <= ord(x) <= 122 else x for x in text.lower()]

def ltnKey(text):
    """
    Description:
    Converts letters into numbers, specifically for cipher keys.
    
    Program Notes:
    Abstraction for other ciphers.
    Gets rid of all non-alphabetic symbols.
    """
    return [ord(x) - 97 for x in text.lower() if 97 <= ord(x) <= 122]

def ntl(nums):
    """
    Description:
    Converts valid numbers into letters.

    Program Notes:
    Abstraction for other ciphers.
    """
    text = ""
    for x in nums:
        if type(x) == int and -1 < x < 26:
            text += str(chr(x + 97))
        else:
            text += str(x)
    return text
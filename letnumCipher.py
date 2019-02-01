def ltnc(text):
    """
    Description:
    A cipher that converts letters to its corresponding number (position in alphabet).

    Doctests:
    >>> ltnc("this is a test")
    '20 8 9 19   9 19   1   20 5 19 20'
    """
    return " ".join(format(ord(x) - 96, "d") if 97 <= ord(x) <= 122 else x for x in text.lower())
    
def ntlc(nums):
    """
    Description:
    A cipher converts valid numbers to its corresponding letter.

    Doctests:
    >>> ntlc()
    """
    text = ""
    last_not_space = True #Gets rid of extra spaces.
    for x in nums.split(" "):
        try:
            if 0 < int(x) < 26:
                text += str(chr(int(x) + 96))
                last_not_space = True
            else:
                text += str(x)
        except:
            if last_not_space and x == "":
                text += " "
                last_not_space = False
            else:
                text += str(x)
                last_not_space = True
    return text
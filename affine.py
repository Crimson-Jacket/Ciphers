from letnum import ltn, ntl

def affine(text, multiplier, shift, encOrDec):
    """
    Description:
    A cipher similar to Caesar Shift, but uses a multiplier to further alter the text. 
    Note that the multiplier MUST be coprime to the alphabet size, as
    using an improper multiplier will result in problems when decoding.

    Program Notes:
    For the boolean variable encOrDec, False will encode text and True will decode text.
    The multiplier inverse is derived by finding a number between 1 and 25 that satisfies this equation:
    number * multiplier % 26 == 1

    Encoding equation:
    (multiplier * [individual letter] + shift) % [alphabet size]
    
    Decoding equation:
    (multiplier inverse * ([individual letter] - shift) % [alphabet size]

    Doctests:
    >>> affine("this is a test!", 3, 15, False)
    'uknr nr p ubru!'
    >>> affine("uknr nr p ubru!", 3, 15, True)
    'this is a test!
    >>> affine("", 1, 3, False)
    ''
    >>> affine("lorem ipsum dolor sit amet", 41, 9, False)
    'slerh zatxh clsle tzi jhri'
    >>> affine("slerh zatxh clsle tzi jhri", 41, 9, True)
    """
    assert any([1 if multiplier % x == 0 else 0 for x in [2, 13, 26]]) != True, "Multiplier must be coprime to 26!"
    assert 0 < shift < 26, "Shift must be between 1 and 25!"
    result = []
    if encOrDec:
        for n in range(1 , 26):
            if n * multiplier % 26 == 1:
                multiplierInverse = n
                break
        formula = (lambda x: (multiplierInverse * (x - shift)) % 26)
    else:
        formula = (lambda x: (multiplier * x + shift) % 26)
    for x in ltn(text):
        if type(x) == int:
            result.append(formula(x))
        else:
            result.append(x)
    return ntl(result)

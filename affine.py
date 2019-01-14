from letnum import ltn, ntl

def affine(text, multiplier, shift, encOrDec):
    """
    Description:
    Basically Caesar Shift with an extra step: a multiplier is used to further alter the text.
    For encOrDec, encoding is False while decoding is True.

    Encoding equation:
    (multiplier * [individual letter] + shift) % [alphabet size]
    
    Decoding equation:
    (([alphabet size] - multiplier) * ([individual letter] + shift)) % [alphabet size]
    """
    assert any([1 if multiplier % x == 0 else 0 for x in [2, 13, 26]]) != True, "Multiplier must be coprime to 26!"
    assert 0 < shift < 26, "Shift must be between 1 and 25!"
    result = []
    formula = (lambda x: (26 - multiplier) * (x - shift) % 26) if encOrDec else (lambda x: (multiplier * x + shift) % 26)
    for x in ltn(text):
        if type(x) == int:
            result.append(formula(x))
        else:
            result.append(x)
    return ntl(result)

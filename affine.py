from letnum import ltn, ntl
def affine(text, multiplier, shift, encOrDec):
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

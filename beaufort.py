from letnum import ltn, ntl, ltnKey

def beaufort(text, key):
    """
    Description:
    A cipher that uses a tabula recta to encode/decode text.
    It's quite similar to Vignere, but its table starts from "Z" rather than "A".

    Equation:
    (key letter - letter) % 26

    Doctests:
    >>> beaufort("this is a test with a weak key.", "key")
    'rxqs wg k lusl cclr k iuku ogg.'
    >>> beaufort("rxqs wg k lusl cclr k iuku ogg.", "key")
    'this is a test with a weak key.'
    >>> beaufort("abc", "defghijklmnop")
    'ddd'
    """
    text = ltn(text)
    key = ltnKey(key)
    result = []
    counter = 0
    for x in text:
        if counter == len(key):
            counter = 0
        if type(x) == int:
            result.append((key[counter] - x) % 26)
            counter += 1
        else:
            result.append(x)
    return ntl(result)
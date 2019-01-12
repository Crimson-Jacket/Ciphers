from letnum import ltn, ntl, ltnKey

def variantBeaufort(text, key, encOrDec):
    text = ltn(text)
    key = ltnKey(key)
    result = []
    counter = 0
    enOrDec = 1 if encOrDec else -1 #True for decode, False for encode
    for x in text:
        if counter == len(key):
            counter = 0
        if type(x) == int:
            result.append((x + (key[counter] * enOrDec)) % 26)
            counter += 1
        else:
            result.append(x)
    return ntl(result)
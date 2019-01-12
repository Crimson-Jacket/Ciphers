from letnum import ltn, ntl, ltnKey

def beaufort(text, key):
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
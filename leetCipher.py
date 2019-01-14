def toLeet(text, pro=False):
    """
    Description:
    Converts text into l33t sp34k.
    Pro mode substitutes the entire alphabet, while regular mode doesn't.
    """
    if pro:
        encoding = {"a":"4", "b":"8", "c":"(", "d":"[)", "e":"3", "f":"|=", "g":"9", "h":"|-|", "i":"1", "j":"_|", "k":"|<", "l":"|_", "m":"|\\/|", "n":"|V", "o":"0", "p":"|*", "q":"(_,)", "r":"|2", "s":"5", "t":"7", "u":"(_)", "v":"\\/", "w":"\\/\\/", "x":"><", "y":"`/", "z":"2"}
        table = str.maketrans(encoding)
        return text.lower().translate(table)
    else:
        letters = "abegiostz"
        symbols = "483910572"
        table = str.maketrans(letters, symbols)
        return text.lower().translate(table)
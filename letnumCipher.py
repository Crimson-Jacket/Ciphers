def ltnc(text):
    return " ".join(format(ord(x) - 96, "d") if 97 <= ord(x) <= 122 else x for x in text.lower())
    
def ntlc(nums):
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
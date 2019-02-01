def toDecimal(text, spaced=False):
    """
    Description:
    Converts ASCII symbols to decimal.
    """
    result = [ord(x) for x in text]
    if spaced:
        return " ".join(result)
    else:
        return "".join(result)

def fromDecimal(nums):
    """
    Description:
    Converts valid decimal to ASCII symbols.
    """
    result = ""
    if " " in nums:
        for el in nums.split(" "):
            result += fromDecimal(el)
    else:
        for i in range(2, len(nums) + 1, 2):
            try:
                result += chr(int(nums[i - 2:i], 2))
            except:
                result += nums[i - (i - 1):i]
        if len(nums) % 2 != 0:
            result += nums[-(len(nums) % 2):]
    return result
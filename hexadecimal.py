def toHex(text, spaced=False):
    """
    Description:
    Converts ASCII symbols into hexadecimal.
    """
    result = [hex(ord(x))[2:] for x in text]
    if spaced:
        return " ".join(result)
    else:
        return "".join(result)

def fromHex(nums):
    """
    Description:
    Converts valid hexadecimal into ASCII symbols.
    """
    result = ""
    if " " in nums:
        for el in nums.split(" "):
            result += fromHex(el)
    else:
        for i in range(2, len(nums) + 1, 2):
            try:
                converted = int("0x" + str(nums[i - 2:i]), 16)
                if 20 <= converted <= 126: 
                    result += chr(converted)
                else:
                    result += nums[i - 2:i]
            except:
                result += nums[i - 2:i]
        if len(nums) % 2 != 0:
            result += nums[-1]
    return result
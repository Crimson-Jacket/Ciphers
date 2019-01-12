def toHex(text, spaced=False):
    result = [hex(ord(x))[2:] for x in text]
    if spaced:
        return " ".join(result)
    else:
        return "".join(result)

def fromHex(nums):
    result = ""
    if " " in nums:
        for el in nums.split(" "):
            result += fromHex(el)
    else:
        for i in range(2, len(nums) + 1, 2):
            try:
                result += chr(int("0x" + str(nums[i - 2:i]), 16))
            except:
                result += nums[i - (i - 1):i]
        if len(nums) % 2 != 0:
            result += nums[-(len(nums) % 2):]
    return result
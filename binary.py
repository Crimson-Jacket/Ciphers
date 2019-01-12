def toBinary(text, spaced=False):
    result = ["00" + format(ord(x), "b") if ord(x) < 64 else "0" + format(ord(x), "b") for x in text]
    if spaced:
        return " ".join(result)
    else:
        return "".join(result)

def fromBinary(nums):
    result = ""
    if " " in nums:
        for el in nums.split(" "):
            result += fromBinary(el)
    else:
        for i in range(8, len(nums) + 1, 8):
            try:
                result += chr(int(nums[i - 8:i], 2))
            except:
                result += nums[i - (i - 1):i]
        if len(nums) % 8 != 0:
            result += nums[-(len(nums) % 8):]
    return result
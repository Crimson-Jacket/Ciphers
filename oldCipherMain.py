"""
def ltn(letters):
    letters = letters.lower()
    nums = ""
    for i in range(len(letters)):
        if letters[i].isalpha():
            nums += str(ord(letters[i]) - 96) + " "
        else:
            nums += letters[i]
    return nums
"""
import sys

#Atbash
def atbash(text):
    nums = [abs(int(x) - 27) if x != "" else " " for x in ltn(text).split(" ")]
    new_nums = ""
    nums.pop()
    for i in nums:
        if i == " ":
            new_nums += " "
        else:
            new_nums += str(i)
            new_nums += " "
    return ntl(new_nums)

#Caesar Shift 
def caesar(text, n):
    nums = [int(x) if x != "" else " " for x in ltn(text).split(" ")]
    new_nums = ""
    for i in nums:
        if i == " ":
            new_nums += " "
        else:
            new_nums += "26" if (i + n) % 26 == 0 else str((i + n) % 26)
            new_nums += " "
    return ntl(new_nums)

#Letters to Binary
def to_binary(text, spaced):
    if spaced == "s":
        return " ".join("0" + format(ord(x), "b") if x != " " else "00100000" for x in text)
    else:
        return "".join("0" + format(ord(x), "b") if x != " " else "00100000" for x in text)

#Binary to Letters
def from_binary(text):
    
    return

#Letters to NumbersS
def ltn(letters):
    return " ".join(format(ord(x) - 96, "d") if x != " " else " " for x in letters.lower())

#Numbers to Letters
def ntl(nums):
    letters = ""
    nums = nums.split(" ")
    for i in range(len(nums)):
        try:
            if 0 < int(nums[i]) < 27:
                letters += str(chr(int(nums[i]) + 96))
            else:
                letters += str(nums[i])
        except:
            if nums[i] == "":
                letters += " "
            else:
                letters += str(nums[i])
    return letters

#Vigenere Encrypt
def vig_encrypt(text, key):
    nums = [int(x) if x != "" else " " for x in ltn(text).split(" ")]
    nums.pop()
    keynums = [int(x) for x in ltn(key).split(" ") if x != ""]
    new_nums = ""
    counter = 0
    for i in nums:
        if counter == len(key):
            counter = 0
        if i == " ":
            new_nums += " "
        else:
            new_nums += "26" if (i + keynums[counter] - 1) % 26 == 0 else str((i + keynums[counter] - 1) % 26)
            new_nums += " "
            counter += 1
    return ntl(new_nums)

#Vigenere Decrypt
def vig_decrypt(text, key):
    nums = [int(x) if x != "" else " " for x in ltn(text).split(" ")]
    nums.pop()
    keynums = [int(x) for x in ltn(key).split(" ") if x != ""]
    new_nums = ""
    counter = 0
    for i in nums:
        if counter == len(key):
            counter = 0
        if i == " ":
            new_nums += " "
        else:
            new_nums += "26" if (i - keynums[counter] + 27) % 26 == 0 else str((i - keynums[counter] + 27) % 26)
            new_nums += " "
            counter += 1
    return ntl(new_nums)

#Encoding/Decoding
def encode_or_decode():
    while True:
        choice = input("Encode or decode: ").lower()
        if choice in ("encode", "e", "en"):
            return True
        elif choice in ("decode", "d", "de"):
            return False
        else:
            print("Please input a valid command.")
        
print("Cipher Program")
while True:
    checker = True
    print("Ciphers: Atbash, Binary, Caesar Shift, Letter Number, Vigenere")
    choice = input("Choose an option or \"exit\" to exit the program: ").lower().strip()
    if choice in ("exit", "e"):
        print("Exiting Program.")
        sys.exit()
    elif choice in ("atbash", "a", "at"):
        text = input("Input text: ").lower()
        print(atbash(text))
    elif choice in ("binary", "b", "bi"):
        if encode_or_decode():
            text = input("Input plain text: ").lower()
            print("Spaced out:",to_binary(text, "s"))
            print("Normal:",to_binary(text, "n"))
        else:
            text = input("Input cipher text: ").lower()
            print(from_binary(text))
    elif choice in ("shift", "caesar", "caesar shift", "c"):
        text = input("Input plain text: ").lower()
        while checker:
            shift = input("Input a shift (range 1-25): ")
            if shift.isdigit() and 0 < int(shift) < 26:
                print(caesar(text, int(shift)))
                checker = False
            else:
                print("Please input a shift.")
    elif choice in ("letternumber", "letter number", "l"):
        while checker:
            if encode_or_decode():
                print(ltn(input("Input plain text: ")))
                checker = False
            else:
                print(ntl(input("Input cipher text: ")))
                checker = False
    elif choice in ("vigenere", "v"):
        while checker:
            if encode_or_decode():
                text = input("Input plain text: ").lower()
                key = input("Input a key: ").lower().strip()
                print(vig_encrypt(text, key))
                checker = False
            else:
                text = input("Input cipher text: ").lower()
                key = input("Input a key: ").lower().strip()
                print(vig_decrypt(text, key))
                checker = False      
    else:
        print("Please input a valid command.")

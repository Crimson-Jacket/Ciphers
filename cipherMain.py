from atbash import atbash
from binary import toBinary, fromBinary
from caesarShift import caesar
from hexadecimal import toHex, fromHex
from letnum import ltn, ltnKey, ntl
from letnumCipher import ltnc, ntlc
from morseCode import toMorse, fromMorse
from vigenere import vigenere

import sys

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
            text = input("Input plain text: ")
            print("Spaced out: ",toBinary(text, True))
            print("Normal: ",toBinary(text))
        else:
            text = input("Input cipher text: ")
            print(fromBinary(text))

    elif choice in ("shift", "caesar", "caesar shift", "c"):
        text = input("Input plain text: ").lower()
        while checker:
            shift = input("Input a shift (range 1-25): ")
            if shift.isdigit() and 0 < int(shift) < 26:
                print(caesar(text, int(shift)))
                checker = False
            else:
                print("Please input a shift.")

    elif choice in ("hexadecimal", "hex", "h"):
        if encode_or_decode():
            text = input("Input plain text:")
            print("Spaced out: ", toHex(text, True))
            print("Normal: ", toHex(text))
        else:
            text = input("Input cipher text: ")
            print(fromHex(text))

    elif choice in ("letternumber", "letter number", "l"):
        if encode_or_decode():
            text = input("Input plain text: ").lower()
            print(ltnc(text))
        else:
            text = input("Input cipher text: ").lower()
            print(ntlc(text))
    
    elif choice in ("morse code", "morse", "m"):
        if encode_or_decode():
            text = input("Input plain text: ")
            print(toMorse(text))
        else:
            text = input("Input cipher text: ")
            print(fromMorse(text))

    elif choice in ("vigenere", "v"):
        if encode_or_decode():
            text = input("Input plain text: ").lower()
            key = input("Input a key: ").lower().strip()
            print(vigenere(text, key, True))
        else:
            text = input("Input cipher text: ").lower()
            key = input("Input a key: ").lower().strip()
            print(vigenere(text, key, False))      
    else:
        print("Please input a valid command.")

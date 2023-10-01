#intelligent life

import numpy as np
import base64

Alice_bases = "+XX+++++++++X+++X+XX++X+++++++XXX++++X+XXX+++X+XXXX+X++X++XXXX++++++X+X+++X+XX++X++++XX+++X+XXXX++XXX+XX+XX++XXX++XXX+X+X+XX+++X+++++++XXX++XXXX+XXXXXXXXX+X+X+X++X+X+++XX+X+XXXX++XX+XXXX++X++XXX+XXXXXX+++++XXX+XX++X+++++X+++XXX+XXX++++XXXXX++X+++XX++++XXX+++X+XX+XXX+X+XXX++XXX++XX++++XXX+X++XX+++XXXX+X+X++++XXX+XXXXX+XXX+X+XXX+XXXX+X+++XXX+X+++++++XX+X++++X++XXXX+++"

Bob_bases = "XX++++++XXXX+XX+XX+X++X++++++X+X++XX+++X+XX++++XXX+X++XXX+++XXX+++X+++XX+XXX+XX+++XX++++XXX++X+X+X++X++X+XX+++++XX+XXXX++XXXX+X+++X+XX+++X++XX+X+X+X++XX+++XXX+X+++++X++++X+XX+X+X+++XXXX++++XXX+XX+X+XXX+XXXXXXX+++XXXX+XX+X++XX+XXXX+X+XXXXX+X+XXX++X+X+++++XXXX++XXX+X+X+XX++X+X+XX++++XXXXXXX++XXXXX+XX+X++X+X++++X+XXX+X+XX+XXXXXXX+X++X++X+X+X+X++++X+X+++X++X+++++X+X++XX"

alice_bits = [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0 , 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]

encrypted_flag = base64.b64decode("UA/JtI3+ZGIHejABkuiel2757g==")

print(encrypted_flag)

"""
Helper Functions!
"""

def stringify(arr): #converts an array of strings/characters into a single string
    s = ""
    for x in arr:
        s += str(x)
    return s
        
def bit_array_to_bytes(bits): #converts an array of bits to an array of bytes (groups of 8 bits)
    return bytearray([int("".join(map(str, bits[i:i+8])), 2) for i in range(0, len(bits), 8)])

def bytes_to_bit_array(bytes): #converts an array of bytes (group of 8 bits) to an array of bits
    return list(''.join(format(ord(byte), '08b') for byte in stringify(bytes)))

def pretty(x): #encodes a bit array
    #return base64.b64encode(bit_array_to_bytes(stringify(x)))
    return base64.b64encode(bit_array_to_bytes(x))

def xor_crypt(key, text):
    if not len(text) <= len(key):
        return "Length Error"
    return list(a^b for a,b in zip(key,text))

out = []

for x in range(len(Alice_bases)):
  if (Alice_bases[x] == Bob_bases[x]):
    out.append(alice_bits[x])

print(stringify(xor_crypt(pretty(out), encrypted_flag)))

#amogus
#fr
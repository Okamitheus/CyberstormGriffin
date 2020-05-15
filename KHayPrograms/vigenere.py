#Katie Hay
#Vigenere Cipher
#Python 2.7.15


import string
from sys import stdin, argv

alphabet = "abcdefghijklmnopqrstuvwxyz "
CapAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

#encryption function
def encrypt(plaintext, key):
    ciphertext = ""
    i=0
    h=0
    k=0
    p=0
    c=0

    #lowercase all characters in key and remove white spaces
    key = key.lower()
    key = key.replace(" ", "")

    #cycling through the plaintext
    while (i < len(plaintext)):

        #if plaintext character is uppercase, encrypt with an uppercase character
        if (plaintext[i].isupper()):
            #key wrap around
            if (h == len(key)): h=0
            else: h=h
            #find the position in the alphabet of k and p
            k = alphabet.index(key[h])
            p = CapAlphabet.index(plaintext[i])
            #encrypt
            c = (k + p)%26
            ciphertext += str(CapAlphabet[c])
            i+=1
            h+=1

        #if plaintext character is lowercase, encrypt with an lowercase character
        elif (plaintext[i].islower()):
            #key wrap around
            if (h == len(key)): h=0
            else: h=h
            #find the position in the alphabet of k and p
            k = alphabet.index(key[h])
            p = alphabet.index(plaintext[i])
            #encrypt
            c = (k + p)%26
            ciphertext += str(alphabet[c])
            i+=1
            h+=1
            
        #if character is a symbol (including spaces), add the symbol to the ciphertext and move on
        else:
            ciphertext += plaintext[i]
            i+=1
            
    return ciphertext

#decryption 
def decrypt(ciphertext, key):
    plaintext = ""
    i=0
    h=0
    k=0
    p=0
    c=0

    #lowercase all characters in key and remove white spaces
    key = key.lower()
    key = key.replace(" ", "")

    #cycling through the plaintext
    while (i < len(ciphertext)):

        #if ciphertext character is uppercase, decrypt with an uppercase character
        if (ciphertext[i].isupper()):
            #key wrap around
            if (h == len(key)): h=0
            else: h=h
            #find the position in the alphabet of k and p
            k = alphabet.index(key[h])
            c = CapAlphabet.index(ciphertext[i])
            #decrypt
            p = (26 + c - k)%26
            plaintext += str(CapAlphabet[p])
            i+=1
            h+=1

        #if ciphertext character is lowercase, decrypt with an lowercase character
        elif (ciphertext[i].islower()):
            #key wrap around
            if (h == len(key)): h=0
            else: h=h
            #find the position in the alphabet of k and p
            k = alphabet.index(key[h])
            c = alphabet.index(ciphertext[i])
            #decrypt
            p = (26 + c - k)%26
            plaintext += str(alphabet[p])
            i+=1
            h+=1
            
        #if character is a symbol (including spaces), add the symbol to the plaintext and move on
        else:
            plaintext += ciphertext[i]
            i+=1

    return plaintext
    
mode = argv[1]
key = argv[2]
text = stdin.read().rstrip("\n")

if (mode == "-e"): print encrypt(text, key)
elif (mode == "-d"): print decrypt(text, key)

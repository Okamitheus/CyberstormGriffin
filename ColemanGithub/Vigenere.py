########################
# Name: Coleman Levy
# Date: 3/24/2020
# Description: a program in Python 2 that encodes and decodes a string
#              using a Vigenere cipher
########################
from sys import stdin, argv

#The function that encrypts the inputted text using the inputted
#key
def encrypt(text, key):
    #The strings that hold the entire alphabet
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = "abcdefghijklmnopqrstuvwxyz"
    #The ints used as iterators
    i = 0
    j = 0
    k = 0
    #The letter being encoded
    tLett = -1
    #The letter from the key being used to encode
    kLett = -1
    #Boolean that indicates if the encoded letter is capital or not
    upper = False
    #The return string
    ciphertext = ""
    #Loops through each character in the inputted string
    while (i < len(text)):
        #Loops through character in the key until a usable letter
        #is found
        while (kLett == -1):
            #Loops through all the capital letters...
            while (j < len(ALPHA)):
                #And if the key has a matching letter, uses it
                if (key[k % len(key)] == ALPHA[j]):
                    kLett = j
                #Moves over one letter at a time
                j += 1
            #Resets iterator
            j = 0
            #Loops through all the lowercase letters...
            while (j < len(alpha)):
                #And if the key has a matching letter, uses it
                if (key[k % len(key)] == alpha[j]):
                    kLett = j
                #Moves over one letter at a time
                j += 1
            #Resets iterator
            j = 0
            
            #Moves one character over on the key
            k += 1
        
        #Loops through all the capital letters...
        while (j < len(ALPHA)):
            #If the encoding text has a matching letter, uses it
            if (text[i] == ALPHA[j]):
                #Sets encoding character to that letter
                tLett = j
                #Indicates the letter is uppercase
                upper = True
            #Moves over one character at a time
            j += 1
        #Resets iterator
        j = 0
        #Loops through all the lowercase letters...
        while (j < len(alpha)):
            #If the encoding text has a matching letter, uses it
            if (text[i] == alpha[j]):
                #Sets encoding character to that letter
                tLett = j
                #Indicates the letter is upper case
                upper = False
            #Moves over one character at a time
            j += 1
        #Resets iterator
        j = 0
        
        #If the current character is a letter...
        if (tLett > -1 and kLett > -1):
            #...and if it is uppercase...
            if (upper):
                #...then encode it as an uppercase letter
                ciphertext += ALPHA[(tLett + kLett) % len(ALPHA)]
            #...otherwise, if it is lowercase...
            else:
                #...then encode it as a lowercase letter
                ciphertext += alpha[(tLett + kLett) % len(alpha)]
        #If it isn't a letter...
        else:
            #Then just add it to the encoded string
            ciphertext += text[i]
            #And go back on the key to reuse the previous letter on it
            k -= 1
        
        #Reset encoding letter and key letter
        tLett = -1
        kLett = -1
        
        #Move over a character on the inputted string
        i += 1

    #Return the encoded string
    return ciphertext

#The function that decrypts the inputted text using the inputted
#key
def decrypt(text, key):
    #The strings that hold the entire alphabet
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = "abcdefghijklmnopqrstuvwxyz"
    #The ints used as iterators
    i = 0
    j = 0
    k = 0
    #The letter being encoded
    tLett = -1
    #The letter from the key being used to encode
    kLett = -1
    #Boolean that indicates if the encoded letter is capital or not
    upper = False
    #The return string
    plaintext = ""
    #Loops through each character in the inputted string
    while (i < len(text)):
        #Loops through character in the key until a usable letter
        #is found
        while (kLett == -1):
            #Loops through all the capital letters...
            while (j < len(ALPHA)):
                #And if the key has a matching letter, uses it
                if (key[k % len(key)] == ALPHA[j]):
                    kLett = j
                #Moves over one letter at a time
                j += 1
            #Resets iterator
            j = 0
            #Loops through all the lowercase letters...
            while (j < len(alpha)):
                #And if the key has a matching letter, uses it
                if (key[k % len(key)] == alpha[j]):
                    kLett = j
                #Moves over one letter at a time
                j += 1
            #Resets iterator
            j = 0
            
            #Moves one character over on the key
            k += 1
        
        #Loops through all the capital letters...
        while (j < len(ALPHA)):
            #If the encoding text has a matching letter, uses it
            if (text[i] == ALPHA[j]):
                #Sets encoding character to that letter
                tLett = j
                #Indicates the letter is uppercase
                upper = True
            #Moves over one character at a time
            j += 1
        #Resets iterator
        j = 0
        #Loops through all the lowercase letters...
        while (j < len(alpha)):
            #If the encoding text has a matching letter, uses it
            if (text[i] == alpha[j]):
                #Sets encoding character to that letter
                tLett = j
                #Indicates the letter is upper case
                upper = False
            #Moves over one character at a time
            j += 1
        #Resets iterator
        j = 0
        
        #If the current character is a letter...
        if (tLett > -1 and kLett > -1):
            #...and if it is an uppercase letter...
            if (upper):
                #...then decode it as an uppercase letter
                plaintext += ALPHA[(26 + tLett - kLett) % len(ALPHA)]
            #...otherwise, if it is a lowercase letter...
            else:
                #...then decode it as an lowercase letter
                plaintext += alpha[(26 + tLett - kLett) % len(alpha)]
        #If it isn't a letter...
        else:
            #Then just add it to the encoded string
            plaintext += text[i]
            #And go back on the key to reuse the previous letter on it
            k -= 1
        
        #Reset encoding letter and key letter
        tLett = -1
        kLett = -1

        #Move over a character on the inputted string
        i += 1

    #Return the decoded string
    return plaintext

#Try to...
try:
    #...see if the string is to be encoded or decoded...
    mode = argv[1]
    #...and see what the key is
    key = argv[2]
#If either are missing...
except:
    #...end the program with an instructional message
    print "You must enter a key and a mode."
    exit(0)

#Text initializes as the string entered into the program minus the
#end line break
text = stdin.read().rstrip("\n")

#If mode is "encrypt"...
if (mode == "-e"):
    #...then encrypt the code
    print encrypt(text, key)
#If mode is "decrypt"
elif (mode == "-d"):
    #...then decrypt the code
    print decrypt(text, key)
#If neither of these...
else:
    #...then end the program with an instructional message 
    print "Must enter a proper mode (-e or -d)"

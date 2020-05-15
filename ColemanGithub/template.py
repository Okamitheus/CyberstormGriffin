# -*- coding: utf-8 -*-
"""
Template for enigma machine challange
See https://py-enigma.readthedocs.io/en/latest/guide.html#building-your-enigma-machine
for more information
"""


from enigma.machine import EnigmaMachine
from sys import stdin, stderr
from time import sleep

#All Wehrmacht models
LIST_OF_ROTORS = ['I','II','III','IV', 'V']
#Kriegsmarine M3 & M4
#LIST_OF_ROTORS = ['I','II','III', 'IV', 'V', 'VI', 'VII', 'VIII']

#X is not in use, to make your life easier
ALPHABET=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']

#there are more reflectors, but this will be bad enough for you to deal with.
LIST_OF_REFLECTORS = ['B', 'C']

#This is one way to create an enigma machine, there are others ;)

Pot_Rotors = []
Pot_Reflector = ['B', 'C']
Pot_Settings = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Pot_Ring = []
RotRot = ['I', 'IV', 'V']

message = stdin.read().rstrip("\n")
text = 0

for boi in RotRot:
    Pot_Rotors.append('II III ' + boi)
    Pot_Rotors.append('III II ' + boi)
    Pot_Rotors.append('II ' + boi + ' III')
    Pot_Rotors.append('III ' + boi + ' II')
    Pot_Rotors.append(boi + ' II III')
    Pot_Rotors.append(boi + ' III II')

for boi in Pot_Settings:
    Pot_Ring.append('W H ' + boi)
    Pot_Ring.append('H W ' + boi)
    Pot_Ring.append('W ' + boi + ' H')
    Pot_Ring.append('H ' + boi + ' W')
    Pot_Ring.append(boi + ' W H')
    Pot_Ring.append(boi + ' H W')

for rot in Pot_Rotors:
    for ring in Pot_Ring:
        machine = EnigmaMachine.from_key_sheet(
            rotors= rot,
            reflector='C',
            ring_settings= ring,
            plugboard_settings='ZM AS QW DF ER CV BN GH TY JK')
        final = machine.process_text(message)
        text = 0
        while(text < len(final)):
            if(final[text: text+8] == 'XROTORSX'):
                print(final.replace("X", " "))
                exit(0)
            text += 1


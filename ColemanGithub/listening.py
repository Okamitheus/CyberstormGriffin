########################
# Name: Coleman Levy
# Date: 3/24/2020
# Description: a program in Python 2 that tries to authenticate a
#              person's identity based on how they type
########################
from pynput.keyboard import Key, Listener
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout

def on_press(key):
    try:
        print key.char.encode("ascii"),
    except AttributeError:
        print str(key)

def on_release(key):
    if (key == Key.esc):
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

tcflush(stdin, TCIFLUSH)

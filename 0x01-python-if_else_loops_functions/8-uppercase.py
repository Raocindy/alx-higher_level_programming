#!/usr/bin/python3
def to_upper(character):
    if 'a' <= character <= 'z':
        return chr(ord(character) - 32)
    else:
        return character

def uppercase(string):
    new_string = ""
    for character in string:
        new_string += to_upper(character)
        print(new_string)

#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            # Convert lowercase to uppercase by subtracting 32 from the ASCII value
            result += chr(ord(char) - 32)
        else:
            # Keep non-lowercase characters as they are
            result += char
    print("{}".format(result))

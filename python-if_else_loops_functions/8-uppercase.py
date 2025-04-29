#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            # Convert lowercase to uppercase by subtracting 32 from the ASCII value
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            # Print non-lowercase characters as they are
            print("{}".format(char), end="")
    print()  # New line after printing the string

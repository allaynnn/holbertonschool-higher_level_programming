#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            # Convert lowercase to uppercase by subtracting 32
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            # For non-lowercase characters, just print the character as is
            print("{}".format(char), end="")
    print()  # Print a new line at the end

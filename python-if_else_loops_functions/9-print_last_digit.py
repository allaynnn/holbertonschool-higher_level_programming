#!/usr/bin/python3
def print_last_digit(number):
    # Ensure the last digit is positive (use absolute value for negative numbers)
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit

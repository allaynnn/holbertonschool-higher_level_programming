#!/usr/bin/env python3
import random
number = random.randint(-10000, 10000)

LastDigit = number % 10 if number > 0
else (abs(number) % 10) * -1

if LastDigit == 0:
    print(f"Last digit of {number} is {LastDigit} and is 0")
elif LastDigit > 5:
    print(f"Last digit of {number} is {LastDigit} and is greater than 5")
else:
    print(f"Last digit of {number} is {LastDigit}", end=" ")
    print("and is less than 6 and not 0")

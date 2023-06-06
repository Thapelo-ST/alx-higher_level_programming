#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    print (f"{number} is negetive")
elif number == 0:
    print ("{} is zero".format(number))
else:
    print (f"{number} is positive")

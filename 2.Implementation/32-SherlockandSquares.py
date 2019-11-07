def squares(a, b):
    roota, rootb = int(a ** (1/2)), int(b ** (1/2))
    return rootb - roota + 1 if roota ** 2 == a else rootb - roota

# OR

# Using math module
from math import *

def squares(a, b):
    return floor(sqrt(b)) - ceil(sqrt(a)) + 1
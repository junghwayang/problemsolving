from math import ceil, sqrt

def encryption(s):
    l = ceil(sqrt(len(s)))
    return ' '.join([s[i::l] for i in range(l)])
def equalizeArray(arr):
    maxcount = 0
    for a in arr:
        if arr.count(a) > maxcount:
            maxcount = arr.count(a)
    return n - maxcount

# OR

# Using Counter module
from collections import Counter

def equalizeArray(arr):
    return n - max(Counter(arr).values())
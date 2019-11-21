# When we need a whole array after rotation
def circularArrayRotation(a, k, queries):
    return [(a[n - (k % n):] + a[:n - (k % n)])[q] for q in queries]

# OR

# When we need just an element at the particular index
def circularArrayRotation(a, k, queries):
    return [a[q - (k % n)] for q in queries]
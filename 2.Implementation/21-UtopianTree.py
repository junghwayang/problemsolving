def utopianTree(n):
    height = 1
    for i in range(1, n+1):
        if i % 2 == 0:
            height += 1
        else:
            height *= 2
    return height

# OR

def utopianTree(n):
    return (2 ** ((n+1)//2 + 1)) - (n % 2) - 1
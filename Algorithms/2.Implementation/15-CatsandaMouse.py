def catAndMouse(x, y, z):
    a = abs(z - x)
    b = abs(z - y)
    return 'Cat A' if a < b else 'Cat B' if a > b else 'Mouse C'
def gcdlcm(n, m):
    a, b = min(n, m), max(n, m)        
    while a > 0:
        temp = a
        a = b % a
        b = temp
    gcd = b
    lcm = gcd * (n // gcd) * (m // gcd)
    return [gcd, lcm]

def getTotalX(a, b):
    lcm, gcd = a[0], b[0]
    for i in range(1, n):
        lcm = gcdlcm(lcm, a[i])[1]
    for i in range(1, m):
        gcd = gcdlcm(gcd, b[i])[0]
    return sum(gcd % (lcm * (i+1)) == 0 for i in range(gcd // lcm))
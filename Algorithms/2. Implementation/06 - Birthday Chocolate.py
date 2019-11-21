def birthday(s, d, m):
    return sum(sum(s[i : i+m]) == d for i in range(n-m+1))
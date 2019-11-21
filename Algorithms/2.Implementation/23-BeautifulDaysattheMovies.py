def beautifulDays(i, j, k):
    return sum((d - int(str(d)[::-1])) % k == 0 for d in range(i, j+1))
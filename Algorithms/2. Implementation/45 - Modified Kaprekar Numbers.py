def kaprekarNumbers(p, q):
    nums = []
    for n in range(p, q+1):
        d, square = len(str(n)), str(n**2)
        l, r = square[:-d], square[-d:]
        if not l:
            l = 0
        if int(l) + int(r) == n:
            nums.append(n)
    if nums:
        print(*nums)
    else:
        print('INVALID RANGE')
def compareTriplets(a, b):
    cnt = [0, 0]
    for i, j in zip(a, b):
        if i > j: cnt[0] += 1
        elif i < j: cnt[1] += 1
    return cnt
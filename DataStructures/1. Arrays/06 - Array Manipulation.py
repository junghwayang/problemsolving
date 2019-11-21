def arrayManipulation(n, queries):
    arr = [0] * n
    for q in queries:
        arr[q[0] - 1] += q[2]
        if q[1] != n:
            arr[q[1]] -= q[2]

    max, add = 0, 0
    for a in arr:
        add += a
        if add > max:
            max = add
    return max
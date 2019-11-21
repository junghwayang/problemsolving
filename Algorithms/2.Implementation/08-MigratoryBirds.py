def migratoryBirds(arr):
    cnt = list(map(lambda x: arr.count(x), range(1, 6)))
    return cnt.index(max(cnt)) + 1
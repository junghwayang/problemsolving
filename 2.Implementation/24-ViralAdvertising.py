def viralAdvertising(n):
    cnt = [2]
    for i in range(n-1):
        cnt.append(cnt[-1] * 3 // 2)
    return sum(cnt)
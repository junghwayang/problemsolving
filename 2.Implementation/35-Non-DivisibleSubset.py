def nonDivisibleSubset(k, s):
    remain = list(map(lambda x: x % k, s))
    ans = 0
    if 0 in remain:
        ans += 1
    remain = [i for i in remain if i != 0]
    cnt = [0] * (k - 1)
    for r in remain:
        cnt[r-1] += 1

    idx = []
    for i in range(k-1):
        maxcnt = max(cnt)
        maxidx = cnt.index(maxcnt) + 1
        if maxcnt > 0 and (k - maxidx) not in idx:
            idx.append(maxidx)
            if (maxidx * 2) % k == 0:
                ans += 1
            else:
                ans += maxcnt
        cnt[maxidx - 1] = 0
    return ans
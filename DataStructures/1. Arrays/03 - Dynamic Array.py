def dynamicArray(n, queries):
    seqList = [[] for _ in range(n)]
    lastAnswer, ans = 0, []
    for q in queries:
        seq = seqList[(q[1] ^ lastAnswer) % n]
        if q[0] == 1:
            seq.append(q[2])
        elif q[0] == 2:
            lastAnswer = seq[q[2] % len(seq)]
            ans.append(lastAnswer)
    return ans
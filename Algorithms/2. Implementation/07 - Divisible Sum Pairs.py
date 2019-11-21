def divisibleSumPairs(n, k, ar):
    return sum((ar[i] + ar[j]) % k == 0 for i in range(n) for j in range(i+1, n))
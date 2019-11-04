from collections import Counter
def sockMerchant(n, ar):
    return sum(map(lambda x: x // 2, Counter(ar).values()))
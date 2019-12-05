def beautifulTriplets(d, arr):
    return sum(a + d in arr and a + 2 * d in arr for a in arr)
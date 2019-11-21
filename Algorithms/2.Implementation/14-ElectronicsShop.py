def getMoneySpent(keyboards, drives, b):
    ans = -1
    for k in keyboards:
        for d in drives:
            if ans < k + d <= b:
                ans = k + d
    return ans

# OR

def getMoneySpent(keyboards, drives, b):
    return max([k + d for k in keyboards for d in drives if k + d <= b] + [-1])
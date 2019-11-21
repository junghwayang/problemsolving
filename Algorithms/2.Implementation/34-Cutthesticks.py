def cutTheSticks(arr):
    ans, shortest = [], 0
    while True:
        ans.append(len(arr))
        shortest = min(arr)
        arr = list(map(lambda x: x - shortest, arr))
        arr = [i for i in arr if i > 0]
        if len(arr) > 0:
            continue
        else:
            break
    return ans

# OR

def cutTheSticks(arr):
    ans, shortest = [], 0
    arr.sort()
    for i, stick in enumerate(arr):
        if stick != shortest:
            ans.append(len(arr) - i)
            shortest = stick
    return ans
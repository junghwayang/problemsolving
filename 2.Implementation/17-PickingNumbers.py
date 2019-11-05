from collections import Counter

def pickingNumbers(a):
    keys, values = list(Counter(sorted(a)).keys()), list(Counter(sorted(a)).values())
    maxvalue = max(values)
    for i in range(len(keys) - 1):
        if keys[i+1] - keys[i] == 1:
            if maxvalue < values[i] + values[i+1]:
                maxvalue = values[i] + values[i+1]
    return maxvalue

# OR

from collections import Counter

def pickingNumbers(a):
    keys, values = list(Counter(sorted(a)).keys()), list(Counter(sorted(a)).values())
    return max([values[i] + values[i+1] for i in range(len(keys) - 1) if keys[i+1] - keys[i] == 1] + [max(values)])


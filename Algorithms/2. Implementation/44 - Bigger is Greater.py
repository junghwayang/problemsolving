def biggerIsGreater(w):
    ans = ''
    for i in range(len(w)-1, 0, -1):
        if w[i] > w[i-1]:
            sortedw, distinctw = sorted(w[i-1:]), sorted(list(set(w[i-1:])))
            next = distinctw[distinctw.index(w[i-1]) + 1]
            sortedw.remove(next)
            ans = w[:i-1] + next + ''.join(sortedw)
            break
    return ans if ans != '' else 'no answer'
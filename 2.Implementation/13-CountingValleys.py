def countingValleys(n, s):
    level = cnt = 0
    for step in s:
        level += 1 if step == 'U' else -1
        if level == 0 and step == 'U':
            cnt += 1
    return cnt
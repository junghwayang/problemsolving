def appendAndDelete(s, t, k):
    match = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            match += 1
        else:
            break
    move = len(s) - match + len(t) - match
    if move > k or ((k - move) % 2 != 0 and k < len(s) + len(t)):
        return 'No'
    else:
        return 'Yes'
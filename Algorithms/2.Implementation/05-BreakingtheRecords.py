def breakingRecords(scores):
    max = min = scores[0]
    cnt = [0, 0]
    for i in scores[1:]:
        if i > max:
            max = i
            cnt[0] += 1
        elif i < min:
            min = i
            cnt[1] += 1
    return cnt
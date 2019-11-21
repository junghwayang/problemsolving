def climbingLeaderboard(scores, alice):
    scores = list(reversed(sorted(set(scores))))
    r, rank = len(scores), []
    for a in alice:
        while (r > 0) and (a >= scores[r - 1]):
            r -= 1
        rank.append(r + 1)
    return rank
def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(sum(x+a in range(s, t+1) for x in apples))
    print(sum(x+b in range(s, t+1) for x in oranges))
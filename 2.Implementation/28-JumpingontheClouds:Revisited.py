def jumpingOnClouds(c, k):
    cloud, e = 0, 100
    while True:
        cloud = (cloud + k) % n
        e -= c[cloud] * 2 + 1
        if cloud == 0:
            break
    return e
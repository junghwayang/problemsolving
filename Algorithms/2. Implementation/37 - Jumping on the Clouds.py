def jumpingOnClouds(c):
    cloud, step = 0, 0
    while cloud < n - 1:
        if cloud + 2 >= n or c[cloud + 2] == 1:
            cloud += 1
            step += 1
        else:
            cloud += 2
            step += 1
    return step
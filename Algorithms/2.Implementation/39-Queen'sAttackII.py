def queensAttack(n, k, r_q, c_q, obstacles):
    up, right, down, left = n - r_q, n - c_q, r_q - 1, c_q - 1
    quad1, quad2, quad3, quad4 = min(up, right), min(up, left), min(down, left), min(down, right)

    for o in obstacles:
        if o[0] == r_q:
            # left
            if o[1] < c_q:
                left = min(left, c_q - o[1] - 1)
            # right
            elif o[1] > c_q:
                right = min(right, o[1] - c_q - 1)

        elif o[1] == c_q:
            # up
            if o[0] > r_q:
                up = min(up, o[0] - r_q - 1)
            # down
            elif o[0] < r_q:
                down = min(down, r_q - o[0] - 1)

        elif abs(o[0] - r_q) == abs(o[1] - c_q):
            if o[0] > r_q:
                # quad1 (up & right)
                if o[1] > c_q:
                    quad1 = min(quad1, o[1] - c_q - 1)
                # quad2 (up & left)
                elif o[1] < c_q:
                    quad2 = min(quad2, c_q - o[1] - 1)
            elif o[0] < r_q:
                # quad3 (down & left)
                if o[1] < c_q:
                    quad3 = min(quad3, c_q - o[1] - 1)
                # quad4 (down & right)
                elif o[1] > c_q:
                    quad4 = min(quad4, o[1] - c_q - 1)
                
    return up + right + down + left + quad1 + quad2 + quad3 + quad4
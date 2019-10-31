def diagonalDifference(arr):
    lefttoright = sum([arr[i][i] for i in range(n)])
    righttoleft = sum([arr[i][-i-1] for i in range(n)])
    return abs(lefttoright - righttoleft)
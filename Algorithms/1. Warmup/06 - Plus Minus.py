def plusMinus(arr):
    print('{0:.6f}'.format(len([i for i in arr if i > 0]) / n))
    print('{0:.6f}'.format(len([i for i in arr if i < 0]) / n))
    print('{0:.6f}'.format(len([i for i in arr if i == 0]) / n))

# OR

def plusMinus(arr):
    print('{0:.6f}'.format(sum([i > 0 for i in arr]) / n))
    print('{0:.6f}'.format(sum([i < 0 for i in arr]) / n))
    print('{0:.6f}'.format(sum([i == 0 for i in arr]) / n))
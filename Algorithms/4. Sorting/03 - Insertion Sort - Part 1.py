def insertionSort1(n, arr):
    temp = arr[-1]
    for i in range(n-2, -1, -1):
        if arr[i] > temp:
            arr[i+1] = arr[i]
            print(*arr)
            if i == 0:
                arr[i] = temp
                print(*arr)
        else:
            arr[i+1] = temp
            print(*arr)
            break
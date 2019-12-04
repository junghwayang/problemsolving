n, arr = int(input()), list(map(int, input().split()))
print(max(a for a in arr if a != max(arr)))

# OR

n, arr = int(input()), list(map(int, input().split()))
print(sorted(set(arr))[-2])
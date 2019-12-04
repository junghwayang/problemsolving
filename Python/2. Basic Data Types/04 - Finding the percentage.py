marks = {}
for _ in range(int(input())):
    line = input().split()
    marks[line[0]] = sum(map(float, line[1:])) / 3
print('%.2f' % marks[input()])
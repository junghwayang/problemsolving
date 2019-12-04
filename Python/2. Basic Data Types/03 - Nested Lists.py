students = sorted([input(), float(input())] for _ in range(int(input())))
low2nd = sorted(set(s[1] for s in students))[1]
for s in students:
    if s[1] == low2nd: print(s[0])

# OR

students = sorted([input(), float(input())] for _ in range(int(input())))
low2nd = sorted(set(s[1] for s in students))[1]
print('\n'.join(name for name, score in students if score == low2nd))
for i in range(int(input())):
    print(i ** 2)

# OR

print(*[i ** 2 for i in range(int(input()))], sep='\n')
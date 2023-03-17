n = 4
for i in range(n):
    for j in range(1, n-i+1):
        print(j, end='  ')
    for j in range(n-i):
        print(' ', end='')
    for j in range(i, 0, -1):
        print(j, end='  ')
    print()


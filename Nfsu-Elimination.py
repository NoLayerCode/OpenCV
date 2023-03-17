def count_nfsu(s):
    count = 0
    while True:
        index = s.find('nfsu')
        if index == -1:
            break
        count += 1
        s = s[:index] + s[index+4:]
    return count

t = int(input())
for _ in range(t):
    s = input()
    count = count_nfsu(s)
    print(count)

def min_transfer_time(s):
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    # count the number of times each character appears in the string
    
    total_time = 0
    for c, freq in count.items():
        if freq == 1:
            total_time += 10
        else:
            total_time += (freq // 2) * 20 + (freq % 2) * 10
            # if the frequency is odd, we need to send one copy with Transfer 1
            # and the rest with Transfer 2; hence the extra 10 seconds
    return total_time

# example usage
t = int(input())
for i in range(t):
    s = input().strip()
    print(min_transfer_time(s))

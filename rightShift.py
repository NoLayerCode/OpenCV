def right_shift(arr):
    n = len(arr)
    max_sum = arr[0] + arr[n-1]
    max_shift = 0
    for i in range(1, n):
        cur_sum = arr[i] + arr[i-1]
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_shift = i
    return arr[-max_shift:] + arr[:-max_shift]

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    shifted_arr = right_shift(arr)
    print(shifted_arr)

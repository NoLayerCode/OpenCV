def maxSumPath(arr):
    n = len(arr) 
    dp = [[0 for j in range(n)] for i in range(n)]
    dp[n-1][n-1] = arr[n-1][n-1]
    for i in range(n-2,-1,-1):
        dp[i][n-1] = arr[i][n-1] + dp[i+1][n-1]
        dp[n-1][i] = arr[n-1][i] + dp[n-1][i+1]
    for i in range(n-2,-1,-1):
        for j in range(n-2,-1,-1):
            dp[i][j] = arr[i][j] + max(dp[i+1][j],dp[i][j+1])
    return dp[0][0]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        row = list(map(int,input().split()))
        arr.append(row) 
    print(maxSumPath(arr))

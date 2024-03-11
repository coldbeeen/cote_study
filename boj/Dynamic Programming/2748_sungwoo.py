from itertools import combinations
t = int(input())

for _ in range(t):
    west, east = map(int, input().split())

    dp = [[0 for _ in range(east + 1)] for _ in range(west + 1)]

    for i in range(1, east + 1):
        dp[1][i] = i

    for i in range(2, west + 1):
        for j in range(i, east + 1):
            for k in range(j, i - 1, -1):
                dp[i][j] += dp[i - 1][k - 1]

    print(dp[n][m])
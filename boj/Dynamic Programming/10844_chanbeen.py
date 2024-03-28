import sys

input = sys.stdin.readline

N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N)]

for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, N):
    for j in range(10):
        if j == 0: #계단 수를 위해서는 끝자리가 0이려면 이전 수가 1이어야함 
            dp[i][j] = dp[i - 1][1]
        elif j == 9: #계단 수를 위해서는 끝자리가 9이려면 이전 수가 8이어야함
            dp[i][j] = dp[i - 1][8]
        else: #끝자리가 아니기때문에 상관없음, j - 1 또는 j + 1이면 됨
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[-1]) % 1000000000)
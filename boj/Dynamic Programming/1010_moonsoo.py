import sys
input= sys.stdin.readline

T = int(input())

dp = [[0 for j in range(31)] for i in range(31)]


# a[3][4] = a[2][3] + a[3][3]
# dp[n] = n-1Cm-1 + nCm-1 = 

for _ in range(T):
    n, m = map(int, input().split())

    dp[n][m] = dp[n-1][m-1] + dp[n][m-1]
import sys

n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(sys.stdin.readline()))

dp = [0 for _ in range(k+1)]
dp[0] = 1

for i, coin in enumerate(coins):
    for K in range(k + 1):
        tmp = K - coin
        if (tmp >= 0):
            dp[K] += dp[tmp]
            tmp -= coin

print(dp[k])
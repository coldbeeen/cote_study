import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (1001)

dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + 2 * dp[i - 2] #2 x 2 타일도 생겼으므로 i - 2에서의 경우의 수가 2배

print(dp[n] % 10007)
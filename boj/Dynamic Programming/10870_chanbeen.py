import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)

if n == 0: #0일 때 예외처리
    pass
else:
    dp[1] = 1

for i in range(2, n + 1): #피보나치 수열
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[-1])
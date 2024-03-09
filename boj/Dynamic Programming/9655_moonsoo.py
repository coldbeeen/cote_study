import sys
input= sys.stdin.readline

N = int(input())

dp = [-1] * 1001
dp[1] = 0 #SK
dp[2] = 1 #CY

for i in range(3, N+1):
    dp[i] = 0 if dp[i-1] == 1 else 1

if dp[N] == 0:
    print("SK")
else:
    print("CY")
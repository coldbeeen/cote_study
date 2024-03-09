import sys
input= sys.stdin.readline

N = int(input())

dp = [-1] * (N + 1)
dp[1] = 'SK'
dp[2] = 'CY'

if N % 2 == 0:
    print('CY')
else:
    print('SK')
import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)

dp[1] = 1 #입력 조건에 따라 0 인덱스는 따로 처리 안 해줘도 됨

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[-1])
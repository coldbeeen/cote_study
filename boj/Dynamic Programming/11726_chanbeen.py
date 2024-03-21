import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (1000 + 1) #길이가 n일 때 2 x n 크기의 직사각형을 채우는 경우의 수
#n은 1000까지

dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n] % 10007)

#가로 길이 기준,
#길이가 1짜리가 추가되어 생기는 경우의 수 + 길이가 2짜리가 추가되어 생기는 경우의 수
import sys

input = sys.stdin.readline

N = int(input())

dp = [[0] * (N + 1) for _ in range(2)] #0으로 끝나는 수, 1로 끝나는 수의 개수 저장하는 배열

dp[1][1] = 1 #1자리 수는 1밖에 없음

for i in range(2, N + 1):
    dp[0][i] = dp[0][i - 1] + dp[1][i - 1] #이전의 수 모두에 0 추가 가능
    dp[1][i] = dp[0][i - 1] #이전에 0으로 끝난 수에만 1 추가 가능

print(dp[0][N] + dp[1][N])
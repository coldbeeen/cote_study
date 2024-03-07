import sys

input = sys.stdin.readline

N = int(input())

limit = 1000 #N의 입력범위는 1000까지
dp = [limit + 1] * (limit + 1) 
dp[0] = 0

stone = [1, 3] #돌을 가져갈 수 있는 경우의 수

for i in range(len(stone)):
    for j in range(stone[i], N + 1):
        if dp[j - stone[i]] != limit + 1:
            dp[j] = min(dp[j], dp[j - stone[i]] + 1)

print('CY' if dp[N] % 2 == 0 else 'SK')

# 상근이가 먼저 시작함
# 돌은 1, 3개씩 가져감 -> 무조건 홀수 개
# N이 짝수라면 무조건 창영이가 이김
# N이 홀수라면 무조건 상근이가 이김
# 1 또는 3개씩 빼는 문제인 듯
# 1, 3개씩 N개를 채울 수 있는 최소 개수를 구해준 뒤, 그 개수가 짝수면 창영, 홀수면 상근이 이긴다
n = int(input())
scores = [0] + [int(input()) for _ in range(n)]
dp = [0 for _ in range(n+1)]

# 1, 2번째 계단의 최대 점수 초기화
dp[1] = scores[1]
if n >= 2:
    dp[2] = scores[1] + scores[2]

for i in range(3, n+1):
    # 1. 직전 칸에서 올라온 경우, 2. 전전 칸에서 올라온 경우
    dp[i] = max(dp[i-3] + scores[i-1] + scores[i], dp[i-2] + scores[i])

print(dp[n])
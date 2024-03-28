n = int(input())
dp = [0 for i in range(n + 1)]
dp[1] = 1

# n > 1에 대해서
# 1. n - 1에서의 이친수에 0 붙이기
# 2. n - 2에서의 이친수에 01 붙이기
# 피보나치 수열로 풀어지는 문제
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])
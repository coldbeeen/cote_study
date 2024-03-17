n = int(input())
dp = [0, 1, 3] + [0 for i in range(n - 2)]  # DP 테이블 세팅

# (2 X (n-1) 직사각형 경우의 수에, 2 X 1 타일 하나 추가)
# + (2 X (n-2) 직사각형 경우의 수에, 2 X 1 타일 두 개 추가 & 2 X 2 타일 추가)
for i in range(3, n + 1):
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[n] % 10007)
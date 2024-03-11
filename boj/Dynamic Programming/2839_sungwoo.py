n = int(input())
dp = [5001 for _ in range(n+5)]  # dp[5] = 1이 가능하도록 n + 5 만큼 DP 테이블 생성
dp[3] = dp[5] = 1  # 3kg와 5kg는 한 봉지에 가능

for i in range(6, n+1):
    dp_min = min(dp[i-3], dp[i-5])  # 1. 3kg 한 봉지를 들었을 때, 2. 5kg 한 봉지를 들었을 때, 의 dp 테이블을 활용해 값 없데이트
    if dp_min != 5001:
        dp[i] = dp_min + 1

print(dp[n] if dp[n] != 5001 else -1)
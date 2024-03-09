import sys
input= sys.stdin.readline

n=int(input())

dp = [-1] * 5001
dp[3] = dp[5] = 1

for i in range(6, n+1):
    if (dp[i-3] < 0) and (dp[i-5] < 0):
        dp[i] = -1
        # 모두 음수이면 dp[n] = -1

    elif dp[i-3] * dp[i-5] < 0:
        dp[i] = max(dp[i-3], dp[i-5]) + 1
        # 둘 중 하나가 음수면 둘 중 최대 +1

    else:
        dp[i] = min(dp[i-3], dp[i-5]) + 1
        # 둘 다 양수면 둘 중 최소 +1

print(dp[n])
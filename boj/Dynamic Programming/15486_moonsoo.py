import sys

n = int(sys.stdin.readline())

consult = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)

for i in range(n-1, -1, -1):
    
    if n - consult[i][0] > i - 1:
        # 남은 날 계산 후 상담 불가하면 넘어감
        dp[i] = max(dp[i + consult[i][0]] + consult[i][1], dp[i+1])

    else:
        dp[i] = dp[i+1]

print(dp[0])
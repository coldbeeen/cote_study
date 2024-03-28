import sys
input = sys.stdin.readline

n = int(input())
consult = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

for i in range(n-1, -1, -1):  # 거꾸로 접근
    if i + consult[i][0] < n + 1:  # 상담일이 n + 1일을 넘지 않는다면
        # (상담 겹치지 않도록) i번째 상담일수 이후의 dp값(누적된 최대 수익)에 현재 상담 금액을 더하여 계산. 그 값이 dp[i+1]보다 작다면 dp[i+1] 값을 취함 (최대 수익을 유지하기 위해)
        dp[i] = max(dp[i+consult[i][0]] + consult[i][1], dp[i+1])
    else:  # 상담일이 n + 1을 넘는다면
        dp[i] = dp[i+1]  # 최근 바로 이전 dp값을 저장
print(dp[0])
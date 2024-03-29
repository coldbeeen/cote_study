#구글링
import sys

input = sys.stdin.readline

N = int(input())

counsel = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 1)

for i in range(N - 1, -1, -1): #맨 끝 날짜부터 거꾸로
    if i + counsel[i][0] < N + 1: #퇴사 전에 i시점에 시작한 상담을 끝낸다면
        dp[i] = max(dp[i + counsel[i][0]] + counsel[i][1], dp[i + 1])
        # dp에는 i시점에서의 최대 상담 수익이 저장된다
        # i일자의 상담이 진행되는 d일 간은 다른 상담을 하지 못 한다
        # 따라서, d일 뒤 시점의 dp값에 i시점의 상담 수익 합산 vs i시점의 상담을 진행 안 하면 얻는 상담 수익
    else: #퇴사 전에 i시점에 시작한 상담을 못 끝낸다면
        dp[i] = dp[i + 1] #이전 값을 그대로 가져간다

print(dp[0])
#약 36분 소요

import sys

input = sys.stdin.readline

N = int(input())

counsel = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 1)

for i in range(N - 1, -1, -1): #상담 일정 역순
    if i + counsel[i][0] > N: #i일에서 상담을 진행하면 퇴사일 오버
        dp[i] = dp[i + 1] #상담 진행 x
    else:
        dp[i] = max(dp[i + 1], counsel[i][1] + dp[i + counsel[i][0]])
    
print(dp[0])

#상담을 통해 N일동안 얻을 수 있는 최대 수익 구하는 문제 -> DP
#대신 역순으로 진행
#i일 기준에서 해당 상담을 진행했을 때 N일이 넘어간다면 상담 X
#안 넘어갈 때만 최대 수익 나올 수 있도록 max 활용하여 dp 갱신
#상담 안 하기 vs counsel[i][1]만큼 수익 얻는 대신 i일부터 counsel[i][0]일 동안 상담하기 (상담하는 중에는 다른 상담 못 함)
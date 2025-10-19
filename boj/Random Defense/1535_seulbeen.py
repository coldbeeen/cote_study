# 1535
# 구글링
# 0-1 배낭문제(dp)
import sys
input=sys.stdin.readline

n=int(input())
hp=[0]+list(map(int,input().split()))
happy=[0]+list(map(int,input().split()))

# 2차원 dp 배열
# dp[i][j]= 체력 J에 I번 사람까지 탐색했을때 최대 행복
dp=[[0]*101 for _ in range(n+1)]

for i in range(n+1):
    for j in range(101):
        # 체력이 남았으면
        if j-hp[i]>=0:
            # dp[i-1][j]: 감사인사를 안하는 경우
            # dp[i-1][j-hp[i]]+ happy[i] : 체력을 깎아서 인사 하는 경우
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-hp[i]]+happy[i])
        # 체력이 남지 않았으면 이전 사람 dp 값 유지
        else:
            dp[i][j]=dp[i-1][j]
# print(hp)
# print(dp)
print(dp[n][99])

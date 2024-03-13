# 연속으로 3계단을 못오름
# n번째 계단을 밟는 경우의 수 = n-2번째 계단을 밟았거나, n-3,n-1번째 계단을 밟았던것
import sys
input=sys.stdin.readline

n=int(input())
score=[0] * (n+1)
dp=[0] * (n+1)

for i in range(1,n+1):
    score[i]+=int(input())
dp[1]=score[1]

for i in range(2,n+1):
    # dp[i-3]+dp[i-1]+score[i]로 헷갈렸었는데, score[i-1]를 더해줘야됨
    dp[i]=max(dp[i-2]+score[i],dp[i-3]+score[i-1]+score[i])
print(dp[n])

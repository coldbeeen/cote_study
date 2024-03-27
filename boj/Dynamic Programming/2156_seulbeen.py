import sys
input=sys.stdin.readline

n=int(input())
wine=[0]*(n+3) # 인덱스 참조 편리용
dp=[0]* (n+3) # 인덱스 참조 편리 및 인덱스 에러 방지용 패딩

for i in range(1,n+1):
    wine[i]+=int(input())

dp[1]=wine[1]
dp[2]=wine[1]+wine[2]

for i in range(3,n+1):
    #dp[i]=max(dp[i-3]+wine[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i],dp[i-1])
    #dp[i]=max(dp[i-3]+wine[i-2]+wine[i],dp[i-2]+wine[i],dp[i-1])
    dp[i]=max(dp[i-3]+wine[i-1]+wine[i],dp[i-2]+wine[i],dp[i-1])
print(dp[n])
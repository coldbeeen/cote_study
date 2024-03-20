# 두개의 타일 케이스가 2개로 나뉘므로 i-1에서 1를 더해 만드는 경우 + i-2에서 2를 더해 만드는 경우 * 2(경우가 두가지)
import sys
input=sys.stdin.readline

n=int(input())

dp=[0]*1001 # limit

dp[1]=1
dp[2]=3

for i in range(3,n+1):
    dp[i]=dp[i-2]*2+dp[i-1]
print(dp[n]%10007)

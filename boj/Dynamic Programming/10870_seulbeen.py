import sys
input=sys.stdin.readline

n=int(input())

dp=[0 for _ in range(n+1)]


if n>0:
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    print(dp[n])

else:
    print(0)
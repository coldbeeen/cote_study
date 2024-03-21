# 최대 경우의 수를 구하는 거니까,,, max로 점화식을 세워야 하나?
#case(n,m)= case(n,m-1)+(n-1,m-1)???
"""
0 0
0 0
0 0
  0
  0
  (3,5)=(3,4)인 케이스 + 동쪽에 돌이 하나 더 생겼으니 양쪽 끝 고정(2,4) 
"""
import sys
input= sys.stdin.readline

t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    dp=[[0 for _ in range(m+1)] for _ in range(n+1)] # dp 배열
    #dp 배열 초기화(nCn, 1Cn)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1:
                dp[i][j]=j
            if i==j:
                dp[i][j]=1

    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1:
                dp[i][j]=j
            else: 
                dp[i][j]=dp[i][j-1]+dp[i-1][j-1]
    print(dp[n][m])

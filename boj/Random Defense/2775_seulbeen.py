# 부녀회장이 될테야
# 30분
"""
a층의 b호에 살려면
a-1층의 b호까지의 사람들의 합이 살아야함
a-1층의 b호 -> a-2층의 1~b호
a-1층의 b-1호는 a-2층의 1~b-1호
0층의 i호에는 i명이 산다
1 2 3 4
1 3 6 10
1 4 10 20
1 5 15 35
1 6 21
1 7 28
결국 a층의 b호는, a층의 b-1호 + a-1층 b호
"""

import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    a=int(input())
    b=int(input())
    #이게 dp?인지는 모르겠지만 아파트 배열 선언, 0층은 초기값 세팅까지
    dp=[[i for i in range(1,b+1)]]+[[0]*(b) for _ in range(a)]
    
    # 문제 로직에 따라 i층의 j호는, i-1층 j호 인원 + i층 j-1호 인원임
    for i in range(1,a+1):
        for j in range(0,b):
            dp[i][j]=dp[i][j-1]+dp[i-1][j]
    
    print(dp[a][b-1])
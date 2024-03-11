# 어쩌다 보니 규칙을 찾았음
# case(n)=case(n-1)+case(n-2)+case(n-3)

"""
    1: 1
    2: 1+1,2 =>2
    3: 1+1+1,1+2,2+1,3 => 4
    4: 7
    5: 13
    6: 24
    7: 44 ?!?!
"""

import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())
    dp=[0,1,2,4]+[0]*(n-3)
    # dp배열 선언 , 3까지 배열 초기화
    for i in range(4,n+1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[n])

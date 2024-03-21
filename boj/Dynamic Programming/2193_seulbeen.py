import sys

input=sys.stdin.readline

n=int(input())

dp=[0]* (n+2) # index 참조 편리성 및 IndexError 방지를 위해 0 패딩 추가
dp[1]=1

for i in range(2,n+1):
    dp[i]=dp[i-2] + dp[i-1]

print(dp[n])

"""
점화식 : case(n)=case(n-1) + case(n-2)

* 끝자리에 1이 오려면 무조건 0이랑 같이(01) 와야됨
case(n-1) : n-1자리의 이친수들에 0을 붙이는 경우
case(n-2) : n-2자리의 이친수들에 01을 붙이는 경우

1: 1
2: 10
3: 100 101
4: 1000, 1010, 1001
5: 10000,10100,10010,10001,10101
"""
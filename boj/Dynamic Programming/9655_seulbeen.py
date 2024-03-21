# 조금 더 DP적으로 생각해보자
import sys
input=sys.stdin.readline

n=int(input())

dp=['SK','CY','SK'] + [0]*(n-3)
flag=['SK','CY']

for i in range(3,n):
    dp[i]='SK' if dp[i-1]=='CY' else 'CY'

print(dp[n-1])
"""
완벽한게임 = 서로 이길라고 하는거 = 어떻게 가져가든 n-1번째 돌을 가져간 애가 짐
초기 조건: [상근,창영,상근] => 항상 완벽한게임이므로..
돌 4개 : [상근,창영,상근,창영]
돌 5개 : [상근,창영,상근,창영,상근]
돌 6개 : [상근,창영,상근.창영,상근,창영]

걍 이거 짝수면 무조건 창영이 이기고 홀수면 무조건 상근이가 이기는데?

import sys
input=sys.stdin.readline

n=int(input())

if n%2==0:
    print("CY")
else:
    print("SK")
"""
# 카드 구매하기 2
# 34분
"""
정답률 75% 치고 어려운데...?
dp에 이중 포문을 쓰는게 맞나 싶은 생각이 발목을 잡음. 사실 별개인데

점화식
dp[i]=min(dp[i],dp[i-j]+cards[j])


dp[i]
1. 기본값
2. i-j개의 카드를 구매하는 이전의 경우 + 카드팩[j]를 사는 경우

1번과 2번을 비교

ex) 
카드 10개를 사는 경우에서 j가 3이라고 가정하면,
dp[7]+card[3]
즉 카드 7개를 사는 현재 최적 값이 dp[7]에 담겨있을 것이고, 거기에 3개짜리 카드팩을 사는 경우의 수
"""
import sys
input=sys.stdin.readline

n=int(input().rstrip())
cards=[0]+list(map(int,input().split()))
# print(cards)
# dp배열의 초기값은, 카드 리스트의 가격 값 복사
dp=cards[:]

for i in range(1,n+1):
    for j in range(1,i):
        dp[i]=min(dp[i],dp[i-j]+cards[j])
print(dp[-1])

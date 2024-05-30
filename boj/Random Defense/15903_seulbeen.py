# 가장 작은거 더하고 갱신...인데
# 실버1에 정답률 40퍼길래 골랐는데 그리디라 그런가 난이도조절에 실패한듯
import sys
input=sys.stdin.readline

n,m=map(int,input().split())

cards=sorted(list(map(int,input().split())))
for _ in range(m):
    sum_of_card=cards[0]+cards[1]
    cards[0] = sum_of_card
    cards[1] = sum_of_card
    cards=sorted(cards)
print(sum(cards))

# 매번 정렬은 무조건 시간초과가 날 것
# bisect 메소드로 일일히 삽입해도 시간초과가 날 것 같았음
# 우선순위큐를 사용해야 될 것 같은데 어떻게 구현해야 하지 하다가 찾아보니 라이브러리가 이미 존재했음
"""
우선순위큐 q=PriorityQueue()
원소삽입: q.put()
원소반환(==pop): q.get()
우선순위큐에는 len 메소드 없음 => q.qsize()
"""

import sys
from queue import PriorityQueue
input=sys.stdin.readline
n=int(input())
total=0
cards=PriorityQueue()

for _ in range(n):
    cards.put(int(input()))

while cards.qsize()>1:
    #카드 두개를 뽑아와서 더함
    card1=cards.get()
    card2=cards.get()
    cnt=card1+card2
    total+=cnt
    # 더한 횟수를 우선순위큐에 다시 집어넣으면 알아서 크기에 맞게 삽입됨
    cards.put(cnt)

print(total)
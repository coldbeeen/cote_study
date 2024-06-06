import sys
from queue import PriorityQueue
import heapq

input = sys.stdin.readline

N = int(input())

cards = PriorityQueue()
for _ in range(N):
    card = int(input())
    cards.put(card)

result = 0
for _ in range(N - 1):
    c1, c2 = cards.get(), cards.get()
    new_card = c1 + c2
    cards.put(new_card)
    
    result += new_card

print(result)


"""
문제:

정렬된 두 묶음의 숫자 카드가 있다고 하자. 각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 번의 비교를 해야 한다.
N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지
----------------------------------------------------------------------------------------------------------------------------
풀이:

주어진 카드 묶음에서 오름차순으로 정렬 후, 가장 앞의 두 개를 합쳐주는 Greedy 방법이다.
이 때, 매 번 더하는 값을 total result에 합쳐서 구했는데 이게 최선인지는 잘 모르겠다.

추가적으로 일반 리스트를 매번 정렬시키면서 하는 것은 시간 초과가 나는 것으로 파악된다.
따라서 우선순위 큐를 사용해서 시간을 단축했다.
"""
from heapq import *

n, m = map(int, input().split())
card_list = list(map(int, input().split()))
heapify(card_list)  # 우선순위 큐 (힙 큐) 변환

for i in range(m):
    sum_of_min_two = heappop(card_list) + heappop(card_list)  # 가장 작은 두 값을 pop하여 합하고
    [heappush(card_list, sum_of_min_two) for _ in range(2)]  # 그 합을 2번 push함

print(sum(card_list))  # 합하여 결과 출력
from heapq import *

def solution(n, works):

    # 야근을 할 필요가 없는 경우
    if sum(works) <= n:
        return 0

    # 힙 자료구조 활용 (최대힙 활용하기 위해 부호를 반대로 초기화)
    max_heap = [-i for i in works]
    heapify(max_heap)

    # n번 만큼 '최댓값에서 1 빼기'를 반복
    for i in range(n):
        heappush(max_heap, heappop(max_heap) + 1)

    # 야근 피로도 계산 및 리턴
    return sum([i ** 2 for i in max_heap])
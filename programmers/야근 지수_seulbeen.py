"""
1. 처음에 반복문으로 배열 훑으면서 최대값으로 계산하니까 시간초과 뜸 => 우선순위큐 써야겠다
2. from queue import PriorityQueue 해도 시간초과가 뜸
3. 구글링 해보니까 heapq로 구현해야 한다고 함
4. heapq가 더 빠르니 코딩테스트에서는 heapq를 사용하라고 함
5. PriorityQueue는 따로 호출을 해줘야 하고 heapq는 가지고있던 리스트를 heapq.heapify(arr)를 통해서 우선순위큐로 만들수 있음
"""
import heapq
def solution(n, works):
    answer = 0
    cnt = 1
    works = [-w for w in works]
    heapq.heapify(works)

    for _ in range(n):
        m_works = heapq.heappop(works)
        m_works = m_works + 1 if m_works < 0 else 0
        heapq.heappush(works, m_works)

    answer = sum([i**2 for i in works])
    return answer


# 시간초과
# from queue import PriorityQueue
# def solution(n, works):
#     answer = 0
#     cnt = 1
#     pq = PriorityQueue()
#     for work in works:
#         pq.put((-work, work))
#     while cnt <= n:
#         m_work = pq.get()
#         # print(f'm_work[0] =  {m_work[0]}')
#         # print(f'put : {(m_work[0]+1,m_work[1]-1)}')
#         pq.put((m_work[0] + 1, m_work[1] - 1))
#         cnt += 1
#     while not pq.empty():
#         piro = pq.get()
#         # print(f'piro = {piro}')
#         if piro[1] >= 0:
#             answer += piro[1] ** 2

#     return answer

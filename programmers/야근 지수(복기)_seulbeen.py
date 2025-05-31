# 11분

import heapq
def solution(n, works):

    # 최소힙으로 최대힙을 동작시켜야 하니 음수로 만들어 줌
    new_works = [-w for w in works]
    heapq.heapify(new_works)

    for _ in range(n):
        
        # 가장 작업량이 많은 작업 pop
        max_work = heapq.heappop(new_works)

        # 해당 작업량이 0보다 작다면(작업이 남아있다면) +1만큼 야근 진행
        max_work += 1 if max_work < 0 else 0

        # 1시간 야근한 결과 heappush
        heapq.heappush(new_works, max_work)
    
    # 야근 지수 계산
    answer = sum([w**2 for w in new_works])
    return answer
"""
<피로도>
현재 남은 작업량의 제곱을 더함
전체 리스트에서 적절히 n을 분배하여 빼며 제곱의 합의 최솟값을 찾는 것이 목표
그런데, '제곱'의 특성상 전체 합을 줄이려면 가장 큰 애들부터 우선순위로 깎아 나가야됨
"""

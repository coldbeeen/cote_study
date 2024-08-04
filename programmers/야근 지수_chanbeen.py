import heapq

def solution(n, works):
    answer = 0

    if n >= sum(works): # 남은 피로도 0
        return answer
    
    works = [-w for w in works]
    heapq.heapify(works)
    
    for _ in range(n):
        tmp = heapq.heappop(works)
        tmp += 1
        
        heapq.heappush(works, tmp)
        
    for i in range(len(works)):
        answer += works[i] ** 2
    
    return answer

# 매 반복문 돌면서 최대값에서 1씩 빼줘야 함
# 매 반복문마다 sort 썼더니 통과 안 됨
# 최대힙으로 변경
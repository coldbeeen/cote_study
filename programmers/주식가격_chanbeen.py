#약 13분 소요

from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        price = queue.popleft()
        
        sec = 0
        
        for q in queue:
            sec += 1
            
            if price > q:
                break 
                
        answer.append(sec)  
        
    return answer

#원소 하나씩 확인하면서 for문으로 돌리는 심플한 방법
#2중 for문 사용하면 시간 초과 날 것 같아서, 첫 for문은 deque로 해결
#첫트에 무난히 통과
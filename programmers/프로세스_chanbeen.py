#약 16분 소요

from collections import deque

def solution(priorities, location):
    answer = 0
    
    array = []
    
    for i in range(len(priorities)):
        array.append([priorities[i], i]) #추후 활용 위해 인덱스도 함께 배열에 저장
        
    queue = deque(array)
    order = [0] * len(priorities)
    
    rank = 1
    max_num = max(queue)[0] #max(queue)를 할 경우 row별 첫 원소의 값이 가장 큰 row가 반환됨 
    
    while queue:
        num, idx = queue.popleft()
        
        if num < max_num:
            queue.append([num, idx]) #우선순위가 낮으면 다시 queue에 넣어줌
        elif num == max_num: #가장 큰 수(우선순위가 가장 높음)
            order[idx] = rank
            rank += 1
            
            if queue: #queue 내 원소가 한 개 남아 있으면, popleft된 후에 queue가 비어 있는 경우 존재
                max_num = max(queue)[0]
    
    return order[location]

#max_num 지정 후 popleft한 num과 비교
#실행 순서를 저장하기 위해 order 배열 생성
#deque 생성 시 order 배열에 순위 저장 위해 인덱스도 함께 넣어줌
#우선순위가 낮으면 큐에 다시 넣고, 우선순위가 가장 높으면 순서를 order배열에 저장 후 max_num 갱신
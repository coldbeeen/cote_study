#약 24분 소요

import heapq

def solution(n, works):
    answer = 0
    
    array = []
    
    for work in works:
        heapq.heappush(array, -work) #최대힙을 위해 -붙임
        
    for _ in range(n):
        to_do = -(heapq.heappop(array)) #가장 큰 값에 -를 붙여야 최소로 pop, 최대힙 구조 구현 가능
        
        if to_do > 0: #일이 남아있을 때 수행
            to_do -= 1
            
        heapq.heappush(array, -to_do)
    
    for num in array:
        answer += num ** 2
    
    return answer

#야근 피로도는 남은 일의 작업량의 제곱 합산
#야근 피로도를 최소화하는 것이 문제
#n번 동안, 매 반복문마다 가장 작업량이 많이 남은 일을 꺼내서 하는 것이 피로도가 최소
#최댓값을 가지는 원소를 뽑기 위해, 최대힙 구조 적용
#약 50분 소요

import heapq

def solution(operations):
    answer = []
    
    heap = []
    heapq.heapify(heap) #최소 힙
    
    for o in operations:
        word, num = o.split(" ")
        
        if word == 'I':
            heapq.heappush(heap, int(num))
        elif word == 'D':
            if heap:
                if num == '1':
                    tmp = []
                    
                    while heap:
                        tmp.append(heapq.heappop(heap))
                    
                    tmp.pop() #마지막 인덱스 pop : 최댓값 제거
                    
                    while tmp:
                        heapq.heappush(heap, tmp.pop())
                        
                elif num == '-1':
                    heapq.heappop(heap)
    
    array = [3, 10, 5, 6, 20, 1]
    heapq.heapify(array)
    
    print(array)
            
    return [max(heap), heap[0]] if heap else [0, 0]

#1차 제출
#heapq 사용한 최소힙 구현으로 인해 최댓값 삭제 시에는 다소 번거로운 코드가 작성됨
#시간 초과는 안 났지만 테스트 케이스 6, 7번에서 틀림

#최소 힙 구조의 조건을 간과해서 발생한 오류였음
#최소 힙 구조의 조건 : "부모 노드의 값이 항상 자식 노드의 값보다 작거나 같다"
#이것이 배열의 마지막 원소가 항상 최댓값을 보장하는 것은 아님
#예시 : [3, 10, 5, 6, 20, 1] 배열을 heapify하면 [1, 6, 3, 10, 20, 5]로 출력됨, 배열의 마지막 원소가 최댓값이 아님
#따라서 최소 힙 구조에서 최댓값은 heap[-1]이 아니라 max(heap)으로 반환해야함
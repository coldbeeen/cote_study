#구글링

import heapq

heap = []

n = int(input())

for _ in range(n):
    numbers = map(int, input().split())
    
    for number in numbers:
        if len(heap) < n: # heap의 크기를 n개로 유지
            heapq.heappush(heap, number)
            
        else:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
                
print(heap[0])

#한 줄씩 입력받아야 메모리 초과 안 남
#뭔가 찜찜한 문제
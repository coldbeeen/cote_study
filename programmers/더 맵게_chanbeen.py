#약 25분 소요

import heapq

def solution(scoville, K):
    def check(array):
        if array[0] >= K:
            return True
        else:
            return False
    
    answer = 0
    
    heapq.heapify(scoville)
    
    if check(scoville):
        return answer
    
    while len(scoville) >= 2:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
    
        new = first + 2 * second
    
        heapq.heappush(scoville, new)
        
        answer += 1
        
        if check(scoville):
            return answer
    
    return -1

#최소 힙 구조 만들고, 2개 pop하여 새로운 스코빌 지수 = 1번째 + 2번째 * 2로 저장
#연산한 결과를 최소 힙 구조에 다시 넣고, #모든 음식의 스코빌 지수가 K 이상인지 체크
#위 과정을 scoville 배열의 길이가 2 이상인 동안 반복

#1차 제출
#테스트 케이스 22, 23 실패
#for문을 도는 check 함수로 인해 효율성 테스트에서 (1948.32ms, 51.8MB)의 성능 기록, 효율성 통과는 일단 됐음
#-1을 반환해야하는 케이스는 잘 됨
#scoville의 길이가 1이 되면서 check를 만족할 경우 반복문이 check까지 안 들어가서 -1를 반환하는 문제 있음

#2차 제출
#문제 해결하니 통과됨, 그러나 check 함수를 효율적으로 짤 방법은 없었을까
#최소 힙 구조니까, scoville[0]만 K 이상이면 모든 요소가 K 이상인 것
#check의 조건문 수정하니 (1739.59ms, 51.7MB)까지 감소
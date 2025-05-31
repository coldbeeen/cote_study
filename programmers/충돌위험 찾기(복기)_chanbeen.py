#약 68분 소요

from collections import Counter

def solution(points, routes):
    def search(route):
        spacetime = []
        
        second = 0
        
        for i in range(1, len(route)):
            start, end = route[i - 1], route[i] #출발 지점부터 최종 도착 지점까지 차례로 순회
            
            startX, startY = points[start - 1]
            endX, endY = points[end - 1]
            
            while startX != endX: #세로 방향 먼저 이동
                spacetime.append((startX, startY, second))

                if startX > endX:
                    startX -= 1
                else:
                    startX += 1

                second += 1

            while startY != endY: #가로 방향 이동
                spacetime.append((startX, startY, second))

                if startY > endY:
                    startY -= 1
                else:
                    startY += 1

                second += 1
        
        spacetime.append((startX, startY, second)) #최종 좌표 도착 후에도 시공간 좌표 추가
        
        return spacetime
        
    answer = 0
    
    cases = []
    
    for route in routes:
        cases.extend(search(route)) #각 로봇별 시공간 좌표 한 리스트에 모두 저장
    
    cnts = Counter(cases) #시공간 좌표별 개수 세기
    
    for key, value in cnts.items():
        if value > 1: #같은 시간, 같은 공간에 로봇이 2개 이상 있었다면 충돌
            answer += 1
    
    return answer

#'충돌' 하려면 같은 좌표, 같은 시간에 로봇이 위치해야함
#가로보다 세로로 먼저 이동, while문 배치 시 참고
#각 로봇당 출발 지점에서 도착 지점까지 향할 때, (현재 x좌표, 현재 y좌표, 현재 시간)의 형태로 저장
#Counter 모듈로 카운트하여, key별 value가 2개 이상이면 충돌한 것이므로 answer에 반영
#한 로봇 당 이동 가능한 포인트가 여러 개인 것에 유의, search 함수 내에서도 for문 필요

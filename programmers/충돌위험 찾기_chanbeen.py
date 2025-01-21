#90분 +@, 구글링

from collections import Counter

def solution(points, routes):
    def search(route):
        second = 0
        
        index_and_time = []
        
        for i in range(1, len(route)):
            startX, startY = points[route[i - 1] - 1]
            endX, endY = points[route[i] - 1] #1번째 포인트의 인덱스는 0이므로 적절히 인덱싱
            
            while startX != endX:
                index_and_time.append((startX, startY, second)) #세로 방향 이동하면서 좌표, 시간 기록
                
                if startX < endX:
                    startX += 1
                else:
                    startX -= 1
                second += 1
            
            while startY != endY:
                index_and_time.append((startX, startY, second)) #가로 방향 이동하면서 좌표, 시간 기록
                
                if startY < endY:
                    startY += 1
                else:
                    startY -= 1
                second += 1
            
        index_and_time.append((startX, startY, second)) #마지막 포인트에 도착했을 때도 충돌이 가능하므로 정보 기록
        #for문 안에 이 코드가 존재 시, 한 로봇이 방문하는 포인트가 3개 이상일 경우 '이전 반복의 end가 이번 반복의 start가 됨 + second는 초기화 안 됨' 이슈로 인해 같은 기록이 리스트에 2번 저장되고, 충돌 위험이 있는 케이스로 잘못 계산되는 문제 존재
        
        return index_and_time
    
    answer = 0
    
    result = []
    
    for route in routes:
        result.extend(search(route)) #각 로봇의 (좌표, 시간)을 하나의 리스트로 다 합치기
    
    result_count = Counter(result) #key : (좌표, 시간), value : 개수
    
    for value in result_count.values():
        if value >= 2: #각 key당 value가 2 이상이면 같은 시공간에 로봇 2 이상 존재, 충돌
            answer += 1
    
    return answer

#시도
#r, c 좌표가 존재하는 bfs 탐색 유형 문제, r과 c는 100까지
#최단 경로가 여러 가지일 경우 r좌표를 우선시, 즉 남북 방향이 우선
#같은 좌표에 로봇 2대 이상 = 충돌
#points : 각 운송 물품의 좌표, routes : 각 로봇의 진행 방향
#bfs로 최단 경로 값은 뽑았는데, 여러 로봇들이 겹치는지는 어떻게 관리하지?
#각 로봇마다 visited를 만들고, 인덱스로 for문을 돌리면서 같은 값을 가지고 있으면 그 인덱스를 같은 시간에 방문한 것이므로 answer + 1하면 될 듯?
#최단경로가 아닌 좌표에 대해서도 카운트가 될 우려가 존재

#구글링
#장애물이 따로 없어서, bfs 방식을 사용하지 않아도 됨
#r이 우선이므로 r -> c 순으로 차례대로 이동시 그게 최단경로
#각 route는 방문하는 지점이 2개 이상이므로 len(route) - 1만큼 for문 돌리면서 start, end 지정해주면 됨
#각 route별로 몇 초에 어느 좌표에 있었는지를 리스트에 모두 담아주고, Counter 모듈을 사용하여 이를 딕셔너리로 바꿔줌
#(x좌표, y좌표, 시간)이 key로 저장되는데, value가 2 이상이라면 로봇끼리 충돌이 발생한 것이므로 answer += 1
#오리지널 dfs/bfs 방식을 매크로처럼 생각하지 않는 마인드가 필요하다고 느낌, 너무 dfs/bfs에만 의존하게 되니 생각의 폭이 좁아지기 때문
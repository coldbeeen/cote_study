#약 32분 소요
#문제 풀이 전 다익스트라 알고리즘 복습 후 진행

import heapq

def solution(N, road, K):
    def dijkstra(start):
        queue = []
        
        heapq.heappush(queue, (0, start)) #비용을 앞에 둬야 비용 기준 최소힙 구조가 생성됨
        
        dist[start] = 0 #자신에 대한 거리 초기화
        
        while queue:
            cost, now = heapq.heappop(queue) #cost : 시작 지점에서 now 지점까지 오는데 든 거리
            
            if cost > dist[now]: #now 지점의 dist 값은 더 작게 갱신되었으므로 재방문 가치 x
                continue
            
            for node in graph[now]: #now 지점과 인접한 지점 탐색
                v, w = node #w : now 지점에서 v 지점으로 가는데 드는 거리
                
                if dist[v] > cost + w: #now 지점에서 v지점으로 가는 것이 더 빠르다면 갱신
                    dist[v] = cost + w
                    heapq.heappush(queue, (cost + w, v)) #갱신 후 다음 탐색을 위해 최소힙에 삽입
        
    answer = 0
    
    graph = [[] for _ in range(N + 1)]
    
    for r in road:
        u, v, w = r
        
        graph[u].append((v, w))
        graph[v].append((u, w)) #양방향 그래프 생성
    
    dist = [1e9] * (N + 1) #초기 거리 무한으로 초기화
    
    dijkstra(1) #시작 지점 입력
    
    for i in range(1, len(dist)):
        if dist[i] <= K:
            answer += 1

    return answer

#그래프 + 간선 가중치 -> 다익스트라 알고리즘
#시작 위치는 1번
#걸린 시간은 K 이하, 본인 포함 카운트
#다익스트라 알고리즘을 복습하고 풀어도 20분 넘게 앓았던 문제
#그래도 이번 기회에 다익스트라는 많이 익숙해진 듯
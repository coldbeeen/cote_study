#60+@, 구글링

import heapq

def solution(N, road, K):
    def dijkstra(v):
        dist[v] = 0
        
        heap = []
        heapq.heappush(heap, (dist[v], v)) #비용을 먼저 저장해야 비용을 기준으로 힙 정렬이 됨
        
        while heap:
            cost, node = heapq.heappop(heap) #최소 힙 구조를 사용하여, 현재 지점에서 가장 적은 비용으로 이동가능한 노드를 먼저 탐색
            
            for c, n in graph[node]: #연결된 노드를 탐색
                if cost + c < dist[n]: #기존 비용보다 더 적게 든다면
                    dist[n] = cost + c
                    
                    heapq.heappush(heap, (cost + c, n)) #비용 갱신 후 최소 힙에 반영
    
    answer = 0
    
    graph = [[] for _ in range(N + 1)]
    dist = [1e9] * (N + 1)
    
    for r in road:
        s, e, c = r
        
        graph[s].append([c, e])
        graph[e].append([c, s]) #양방향 연결
    
    dijkstra(1)
    
    for i in range(1, N + 1):
        if dist[i] <= K:
            answer += 1

    return answer

#1차 제출
#DFS/BFS
#1번 노드에서 탐색 시작
#N번 노드에 도달했을 때, 비용이 K 이하라면 N번 노드에는 배달 가능
#1 -> N 경로의 비용 계산 결과가 K 이상일 때 방문처리를 한다면, 다른 가능한 경로가 있어도 카운트가 안 될 우려 존재
#BFS로 노드별 최소 비용을 다 기록하고, 이후 for문으로 배달 가능한 노드만 골라내기
#59.4점
#BFS는 간선의 가중치가 모두 같을 때만 사용가능하다고 함, 본 문제에서는 BFS 사용 불가

#구글링
#다익스트라 알고리즘
#간선에 가중치가 존재할 경우 동서남북에 각각 (3, 2, 4, 1) 노드가 존재하는 다이아몬드형 그래프를 가정했을 때
#BFS는 무조건 너비 탐색이므로 1 -> (2, 3) -> 4 이지만
#Dijkstra는 1 -> 3 -> 4 -> 2 순서로 탐색도 가능함
#BFS는 이미 방문한 지점을 다시 못 방문하므로 간선에 가중치가 존재하면 고려 못 하는 케이스가 생길 수 밖에 없음
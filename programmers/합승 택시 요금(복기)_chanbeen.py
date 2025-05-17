#약 55분 소요

import heapq

def solution(n, s, a, b, fares):
    def dijkstra(start):
        distances = [INF] * (n + 1)
        queue = []
        
        distances[start] = 0
        heapq.heappush(queue, (0, start))
        
        while queue:
            cost, now = heapq.heappop(queue)
            
            if cost > distances[now]:
                continue
                
            for node in graph[now]:
                v, w = node
                
                if distances[v] > cost + w:
                    distances[v] = cost + w
                    heapq.heappush(queue, (cost + w, v))
        
        return distances
        
    INF = 1e9
    answer = INF
    
    graph = [[] for _ in range(n + 1)]
    
    for fare in fares:
        u, v, c = fare
        
        graph[u].append((v, c))
        graph[v].append((u, c))
    
    Ds = [0] + [dijkstra(i) for i in range(1, n + 1)]
    
    for i in range(1, n + 1):
        answer = min(answer, Ds[s][i] + Ds[i][a] + Ds[i][b])
    
    return answer

#존재하는 각 지점 i에 대해 s부터 i까지 합승했다고 가정하여 최소 케이스 구하기
#s에서 i + i에서 a + i에서 b 거리가 가장 작은 값 반환
#간선에 가중치가 존재하므로, 다익스트라 알고리즘 사용
#다익스트라 내에서 i를 출발 지점으로 두고, s, a, b까지 가는 최소 거리를 구해줌
#각 노드에 대한 다익스트라를 수행하여 2차원 리스트 생성

#그래프 만들 때 u, v대신 s, e 넣었다가 입력 변수 s랑 겹쳐서 엇갈렸음. 찾는데 20분 씀
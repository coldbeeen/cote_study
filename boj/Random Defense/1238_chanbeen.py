#약 30분 소요

import heapq

def dijkstra(v):
    dist = [float('inf')] * (N + 1)
    
    queue = []
    
    heapq.heappush(queue, (0, v))
    
    dist[v] = 0
    
    while queue:
        curr_cost, curr_node = heapq.heappop(queue)
        
        for node, cost in graph[curr_node]:
            if dist[node] > curr_cost + cost:
                dist[node] = curr_cost + cost
                heapq.heappush(queue, (curr_cost + cost, node))
                
    return dist

N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, c = map(int, input().split())
    
    graph[s].append((e, c)) #단방향
    
values = dijkstra(X) # X -> 각자 마을
values[0] = 0 #inf 처리

for i in range(1, N + 1):
    if i != X:
        value = dijkstra(i)
        
        values[i] += value[X] #i마을 -> X(파티장) 최단거리
        
print(max(values))

#각자 마을에서 파티장 X까지 오고가는 거리가 가장 긴 사람 구하는 문제
#단방향 + 간선 가중치 -> 다익스트라
#파티장 -> 집 : X 시점 다익스트라
#각자 집 -> 파티장 : 각자 i 시점 다익스트라 (X 시점일 때는 제외 필요)
#골3치고는 직관적이었던 문제
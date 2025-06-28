#약 71분 소요

import sys
import heapq

def dijkstra(v):
    queue = []

    dist[v] = 0

    heapq.heappush(queue, (0, 0))

    while queue:
        curr_cost, curr_node = heapq.heappop(queue)

        for n, c in graph[curr_node]:
            cost = dist[curr_node] + c

            if dist[n] > cost:
                dist[n] = cost
                heapq.heappush(queue, (cost, n))

input = sys.stdin.readline

N, D = map(int, input().split())

graph = [[] for _ in range(D + 1)] #고속도로 내 모든 지점을 노드로 가지는 그래프

for i in range(D):
    graph[i].append((i + 1, 1)) #옆 지점으로 가는 경로 : 1

for _ in range(N):
    start, end, cost = map(int, input().split())
    
    if end <= D: #고속도로 길이보다 지름길 도착점이 짧아야 함
        graph[start].append((end, cost))

dist = [1e9] * (D + 1)

dijkstra(0)

print(dist[-1])

#단뱡향, 가중치, 최단 경로 -> 다익스트라
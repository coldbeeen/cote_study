#약 20분 소요

import heapq

def dijkstra(start):
    distances = [float('inf')] * (N + 1)
    distances[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))  # (거리, 노드)

    while queue:
        curr_dist, curr_node = heapq.heappop(queue)

        for node, cost in graph[curr_node]:

            dist = curr_dist + cost

            if dist < distances[node]:
                distances[node] = dist
                heapq.heappush(queue, (dist, node))

    return distances

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))
    graph[b].append((a, c))

result = dijkstra(1)

print(result[N])

#다익트스트라 알고리즘을 사용하여 최단 경로를 찾는 문제
# 파티
# 1750
"""
다익스트라인가... 플로이드인가... 그것이 문제로다...
다익스트라를 그냥 두번 쓰면 되는것 같기도 하고
"""

import sys
import heapq

input = sys.stdin.readline
T = float("inf")
N, M, X = map(int, input().split())
# print(N,M,X)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, d = map(int, input().split())
    graph[s].append((d, e))


# print(graph)
def dijkstra(start):
    q = []
    distance = [T for _ in range(N + 1)]
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        d, n = heapq.heappop(q)
        # print(d,n)

        for dist, node in graph[n]:
            if d + dist < distance[node]:
                distance[node] = d + dist
                heapq.heappush(q, (d + dist, node))
    return distance

distance_list = [[0]]
result = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    distance_list.append(dijkstra(i))

print(distance_list)
for i in range(1, N + 1):
    result[i] = distance_list[i][X] + distance_list[X][i]
print(result)
print(max(result[1:]))

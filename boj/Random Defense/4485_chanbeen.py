#약 41분 소요

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0)) #cost, x, y
    
    dist[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if x == n - 1 and y == n - 1: #끝 지점에 도달했으므로 break
            print(f'Problem {cnt}: {dist[x][y]}')
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + graph[nx][ny]

                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 1

while True:
    n = int(input())
    
    if n == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]

    dijkstra()
    cnt += 1
    
#bfs로 풀릴 줄 알았으나 아니었음
#도둑루피를 가중치로 사용해서, 다익스트라 알고리즘을 적용하면 풀리는 문제
#연결된 그래프가 아닌 사방 탐색이므로 dx dy 추가 활용 필요
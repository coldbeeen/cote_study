#약 28분 소요

import heapq

def dijkstra(a, b):
    distance[a][b] = 0
    
    queue = []
    heapq.heappush(queue, (0, a, b))

    while queue:
        curr_dist, x, y = heapq.heappop(queue)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                cost = curr_dist + maze[nx][ny]

                if distance[nx][ny] > cost:
                    distance[nx][ny] = cost

                    heapq.heappush(queue, (cost, nx, ny))

    

M, N = map(int, input().split())

maze = [list(map(int, list(input()))) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

distance = [[float('inf')] * M for _ in range(N)]

dijkstra(0, 0)

print(distance[N - 1][M - 1])

#0은 빈 방, 1은 벽
#왼쪽 맨 위에서 시작, 오른쪽 맨 아래로 이동
#최소 경로를 구하는 것이 아닌, 1을 가장 적게 만나는 경우의 수를 찾는 문제
#벽이 있는 곳을 가중치 1을 지닌 노드로 생각
#이후 다익스트라 알고리즘 적용하여 (N, M)까지의 최단 경로 구하기

#이전에 비교적 유사한 로직의 문제를 풀었던 경험이 있어서, 무난하게 푼 듯
#젤다 문제였던 듯?
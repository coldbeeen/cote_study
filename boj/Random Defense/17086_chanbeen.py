from collections import deque

def bfs(a, b):
    visited = [[-1] * M for _ in range(N)]
    visited[a][b] = 0

    queue = deque([(a, b)])

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not sharks[nx][ny]:
                    if visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))

    for i in range(N):
        for j in range(M):
            if visited[i][j] < result[i][j]:
                result[i][j] = visited[i][j]


N, M = map(int, input().split())

sharks = [list(map(int, input().split())) for _ in range(N)]

result = [[float('inf')] * M for _ in range(N)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(N):
    for j in range(M):
        if sharks[i][j]:
            bfs(i, j)

max_result = 0

for i in range(N):
    for j in range(M):
        if max_result < result[i][j]:
            max_result = result[i][j]

print(max_result)
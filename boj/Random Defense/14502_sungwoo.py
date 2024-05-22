from itertools import combinations
from copy import deepcopy

def dfs(x, y):  # DFS 수행 (1이라는 값을 벽이자 방문한 곳으로 간주)
    graph[x][y] = 1  # 방문 처리

    for i in range(4):  # 상하좌우 탐색
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:  # 갈 수 있다면
            dfs(nx, ny)  # DFS 수행

n, m = map(int, input().split())
original_graph = [list(map(int, input().split())) for _ in range(n)]

# 벽을 세울 수 있는 좌표(0인 좌표) 생성
candidates = []
for i in range(n):
    for j in range(m):
        if original_graph[i][j] == 0:
            candidates.append((i, j))

result = 0
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

# 위에서 구한 좌표를 통해 3개의 좌표로 구성된 조합을 생성하여 DFS를 수행함 (안전 구역 최댓값을 result에 저장)
for candidate in combinations(candidates, 3):
    graph = deepcopy(original_graph)  # 원본 그래프를 graph에 복사

    for i, j in candidate:  # 3개의 벽 세우기
        graph[i][j] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:  # 바이러스에서 DFS 수행
                dfs(i, j)

    result = max(result, sum([row.count(0) for row in graph]))  # 0의 개수가 안전 구역 개수

print(result)
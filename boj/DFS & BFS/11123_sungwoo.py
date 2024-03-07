import sys
sys.setrecursionlimit(10**5)
t = int(input())

def DFS(x, y):
    graph[x][y] = '.'  # 방문 표시를 풀로 바꾸어 표시
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    for i in range(4):  # 상하좌우
        nx, ny = x + dx[i], y + dy[i]  # 다음 위치 후보

        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == '#':  # 유효한 위치이고, 양이라면
            graph[nx][ny] = '.'  # 방문 표시
            DFS(nx, ny)  # DFS 재귀


for _ in range(t):
    h, w = map(int, input().split())
    graph = [list(input()) for _ in range(h)]

    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '#':  # 양이라면 DFS 시작!
                DFS(i, j)
                result += 1  # 양 무리 증가

    print(result)


import sys
sys.setrecursionlimit(10**6)  # 재귀 최대 깊이 설정
input = sys.stdin.readline

def DFS(x, y):  # 깊이 우선 탐색
    graph[x][y] = -1  # 방문 처리

    for i in range(8):  # 모든 방향을 탐색
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:  # 유효한 인덱스이고 땅이라면 방문 (재귀)
            DFS(nx, ny)

# 걸어갈 수 있는 방향 설정
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    w, h = map(int, input().split())

    if w == h == 0:  # 케이스 입력 종료 조건
        break

    graph = [list(map(int, input().split())) for _ in range(h)]  # 그래프 생성
    result = 0

    for i in range(h):  # 모든 좌표 탐색
        for j in range(w):
            if graph[i][j] == 1:  # 해당 위치가 땅이라면
                DFS(i, j)  # DFS 함수를 통해 섬 하나를 탐색하게 됨
                result += 1

    print(result)
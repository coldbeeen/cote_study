import sys
input = sys.stdin.readline
sys.setrecursionlimit(5000)  # 재귀 최대 깊이 5000으로

t = int(input())

def search_group(r, c):  # DFS 형태의 탐색
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):  # 상하좌우 탐색
        nx, ny = r + dx[i], c + dy[i]  # 다음 좌표 설정
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:  # 유효한 위치이고, 배추라면 재귀
            graph[nx][ny] = 0  # 방문 처리(0으로 업데이트하여 추후 방문이 안되게 함)
            search_group(nx, ny)  # 다음 좌표로 재귀

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):  # 그래프를 만들어 배추 위치에 1로 표시
        c, r = map(int, input().split())
        graph[r][c] = 1

    result = 0
    for r in range(n):  # 모든 좌표를 순회하며
        for c in range(m):
            if graph[r][c] == 1:  # 배추라면
                search_group(r, c)  # 그룹 탐색 시도
                result += 1  # 결과값 1 증가

    print(result)
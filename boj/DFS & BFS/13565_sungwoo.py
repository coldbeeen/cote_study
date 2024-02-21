import sys
sys.setrecursionlimit(10**6)  # 재귀 최대 깊이 설정

def valid(x, y):  # 유효한 위치인지 검사 (그래프 내 위치, 미방문, 전류 통함)
    if 0 <= x < m and 0 <= y < n and not visited[x][y] and graph[x][y] == 0:
        return True
    return False

def DFS(x, y):  # DFS 탐색
    global percolated
    if x == m - 1:  # 침투(percolate)하였다면
        percolated = True  # 침투 여부 True 설정 후 DFS 종료
        return

    visited[x][y] = True  # 현재 위치 방문 처리
    dx,  dy = [1, -1, 0 ,0], [0, 0, 1, -1]  # 다음 위치 탐색을 위한 변수

    for i in range(4):  # 상하좌우 시도
        nx, ny = x + dx[i], y + dy[i]  # 다음 위치
        if valid(nx, ny):  # 유효한 위치라면 (그래프 내 위치, 미방문, 전류 통함)
            DFS(nx, ny)  # 재귀
            if percolated:  # 침투하였다면 DFS 종료
                return


m, n = map(int, input().split())
graph = [list(map(int, input())) for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]

percolated = False  # 침투(percolate)하였는지 확인하기 위한 변수

for i in range(n):  # 바깥쪽에서 전류를 흘려보냄 (graph[0][:])
    DFS(0, i)  # DFS 수행
    if percolated:  # 침투하였다면 YES 출력 후 종료
        print("YES")
        break
else:  # 끝까지 침투하지 못했다면 NO 출력
    print("NO")

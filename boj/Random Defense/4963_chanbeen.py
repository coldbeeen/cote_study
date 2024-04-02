import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6) #dfs로 풀 때는 무조건 설정

def dfs(x, y):
    visited[x][y] = 1 #방문 처리
    
    for i in range(8): #8방향
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < h and 0 <= ny < w:
            if map_array[nx][ny] == 1: #근처 지역이 섬이고
                if visited[nx][ny] == 0: #방문 안 했다면
                    dfs(nx, ny) #재귀 호출

#대각선으로 연결되어 있어도 갈 수 있는 섬
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]
# 서 동 남 북 북서 남서 북동 남동

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0: #종료 조건
        break
    
    map_array = [list(map(int, input().split())) for _ in range(h)]
    
    visited = [[0] * w for _ in range(h)]
    
    island = 0
    
    for i in range(h):
        for j in range(w):
            if map_array[i][j] == 1: #해당 좌표가 섬이고
                if visited[i][j] == 0: #아직 방문 안 했다면
                    dfs(i, j)
                    island += 1 #하나의 연결된 섬에 대해서 방문 처리 왼료
                    
    print(island)

#섬의 개수 세기 : DFS
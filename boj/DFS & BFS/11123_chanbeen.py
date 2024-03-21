import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(x, y):
    visited[x][y] = True #방문 처리
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < H and 0 <= ny < W:
            if graph[nx][ny] == '#': #한 무리의 양
                if not visited[nx][ny]: #아직 방문하지 않았음 
                    DFS(nx, ny)

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] #서 동 남 북

for _ in range(T):
    H, W = map(int, input().split())
    
    graph = [list(input().rstrip()) for _ in range(H)]
    
    visited = [[False for _ in range(W)] for _ in range(H)]
    
    cnt = 0
    
    for i in range(H):
        for j in range(W):
            if graph[i][j] == '#':
                if not visited[i][j]:
                    DFS(i, j)
                    cnt += 1 #무리 개수 카운트
    
    print(cnt)
    
    #14, 15번 라인과 34, 35번 라인에서 조건문 내용이 겹친다
    #좀 더 효율적으로 코드를 짤 수는 없었을까?
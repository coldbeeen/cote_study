import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6) 

def DFS(x, y):
    graph[x][y] = 0 #방문 처리
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M: #범위 체크 필수
            if graph[nx][ny] == 1:
                DFS(nx, ny)
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] #서 동 남 북

for _ in range(int(input())):
    cnt = 0
    M, N, K = map(int, input().split())
    
    graph = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        m, n = map(int, input().split())
        graph[n][m] = 1
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                DFS(i, j) 
                cnt += 1 #인접한 배추를 다 지워가면서 DFS가 호출되는 횟수를 카운트
    print(cnt)
#약 15분 소요

from collections import deque

def bfs(a, b):
    visited[a][b] = True
    
    queue = deque([[a, b]])
    
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    if array[nx][ny] == '#':
                        visited[nx][ny] = True
                        cnt += 1
                        queue.append([nx, ny])
                        
    results.append(cnt) #뭉쳐진 쓰레기의 크기

N, M, K = map(int, input().split())

array = [['.'] * M for _ in range(N)]

visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(K):
    r, c = map(int, input().split())
    
    array[r - 1][c - 1] = '#' #쓰레기 좌표

results = []

for i in range(N):
    for j in range(M):
        if not visited[i][j] and array[i][j] == '#':
            bfs(i, j)
            
print(max(results))

#가장 큰 크기를 구하는 클래식한 그래프 순회 문제
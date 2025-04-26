#약 14분 소요

from collections import deque

def solution(maps):
    def bfs(a, b):
        visited[a][b] = 1
        
        queue = deque([[a, b]])
        
        while queue:
            
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] == 1:
                        if visited[nx][ny] == -1:
                            visited[nx][ny] = visited[x][y] + 1
                            queue.append([nx, ny])
                            
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[-1] * m for _ in range(n)]
    
    bfs(0, 0)
    
    return visited[n - 1][m - 1]

#클래식한 그래프 탐색 문제
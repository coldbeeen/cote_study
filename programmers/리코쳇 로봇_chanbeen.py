#약 42분 소요

from collections import deque

def solution(board):
    def bfs(a, b, c):
        visited[a][b] = 0 #시작점 초기화
        
        queue = deque([[a, b, c]])
        
        while queue:
            x, y, cost = queue.popleft()
            
            if board[x][y] == 'G':
                return cost
            
            for i in range(4):
                nx = x
                ny = y
                
                while 0 <= nx + dx[i] < m and 0 <= ny + dy[i] < n and board[nx + dx[i]][ny + dy[i]] != 'D': #꼭짓점이거나 장애물에 걸릴 때까지 슬라이딩
                    nx += dx[i]
                    ny += dy[i]
                
                if visited[nx][ny] > cost + 1: #방문 안 했던 곳과 방문 했지만 움직인 거리가 더 길었던 경우를 한 번에 관리 가능
                    visited[nx][ny] = cost + 1
                    queue.append([nx, ny, cost + 1])
                    
        return -1 #bfs 순회할 동안 G에 못 도달 했다는 뜻
    
    m = len(board) #세로
    n = len(board[0]) #가로
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'R':
                start_x, start_y = i, j #시작 위치 찾기
                break
    
    visited = [[float('inf')] * n for _ in range(m)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    return bfs(start_x, start_y, 0)

#bfs 슬라이딩 조건문 부분과 visited 배열을 최댓값으로 초기화한 후 cost로 관리하도록 구현하는 곳에서 시간 소요
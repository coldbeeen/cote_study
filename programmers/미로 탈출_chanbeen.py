#약 25분 소요

from collections import deque

def solution(maps):
    def bfs(start, end):
        m = len(maps)
        n = len(maps[0])
    
        visited = [[False] * n for _ in range(m)] #bfs를 2번 호출하므로, bfs 안에서 각각 선언해줘야됨
    
        dx = [-1, 1, 0, 0]
        dy = [0, 0 , -1, 1]
        
        queue = deque()
    
        for i in range(m):
            for j in range(n):
                if maps[i][j] == start: #출발 지점 찾기
                    queue.append([i, j, 0])
                    break
        
        while queue:
            x, y, cost = queue.popleft()
            
            if maps[x][y] == end: #도착했으면 비용 반환
                return cost
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] != 'X':
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append([nx, ny, cost + 1])
        
        return -1 #탈출 경로 존재 x
    
    num1 = bfs('S', 'L')
    num2 = bfs('L', 'E')
    
    if num1 == -1 or num2 == -1: #해당하면 경로가 없는 것
        return -1
    else:
        return num1 + num2
    
#레버를 들렀다가 출구로 가야되므로, bfs의 출발지와 목적지를 설정하여 2번 수행하면 되는 문제
#비용을 visited 배열의 값으로 관리하는 대신 변수로 관리해주니 더 편한 느낌
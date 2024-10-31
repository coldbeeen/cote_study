from collections import deque

def solution(land):
    def bfs(a, b):
        visited[a][b] = 1
        
        queue = deque([[a, b]])
        
        cnt = 1
        min_y = max_y = b
        
        while queue:
            x, y = queue.popleft()
            
            min_y = min(min_y, y)
            max_y = max(max_y, y) #한 석유 덩어리가 min_y 열부터 max_y 열까지 있다고 생각
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] == 0 and land[nx][ny] == 1:
                        cnt += 1
                        visited[nx][ny] = 1
                        queue.append([nx, ny])
            
        for i in range(min_y, max_y + 1):
            result[i] += cnt #한 석유 덩어리에 대해서는 min_y ~ max_y 열에서 시추관을 꽂을 경우 다 얻을 수 있음
    
    n = len(land)
    m = len(land[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[0] * m for _ in range(n)]
    result = [0] * len(land[0]) #하나의 인덱스가 각 열을 나타냄
    
    for j in range(m):
        for i in range(n):
            if land[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
    
    return max(result)

# 모든 칸을 다 돌면서 조건부 DFS를 시도하니 효율성에서 시간 초과 발생
#약 12분 소요

from collections import deque

def solution(maps):
    def bfs(a, b):
        visited[a][b] = True
        
        queue = deque([[a, b]])
        
        food = maps_list[a][b]
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m:
                    if maps_list[nx][ny] != 'X': #무인도
                        if not visited[nx][ny]: #아직 방문 X
                            visited[nx][ny] = True
                            food += maps_list[nx][ny]
                            queue.append([nx, ny])
            
        return food
    
    answer = []
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    maps_list = []
    
    for i in range(n): #주어진 문자열 리스트로 변환
        tmp = list(maps[i])
        
        for j in range(len(tmp)):
            if tmp[j] == 'X':
                continue
            else:
                tmp[j] = int(tmp[j]) #식량 합산을 위해 int 변환
        
        maps_list.append(tmp)
    
    for i in range(n):
        for j in range(m):
            if maps_list[i][j] != 'X':
                if not visited[i][j]:
                    answer.append(bfs(i, j))
                    
    if len(answer) == 0: #무인도 없으면 예외처리
        answer.append(-1)
    else:
        answer.sort()
    
    return answer

#클래식한 그래프 순회 문제, 무난히 통과
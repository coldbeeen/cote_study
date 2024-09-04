#구글링
from collections import deque

def solution(board):
    def bfs(dir):
        N = len(board)
        price = [[float('inf')] * N for _ in range(N)]
        
        price[0][0] = 0 #초기 비용
        
        queue = deque([(0, 0, 0, dir)]) #x좌표, y좌표, 비용, 진행방향
        
        while queue:
            x, y, c, d = queue.popleft()
            
            if x == N - 1 and y == N - 1:
                continue
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                nd = i
                
                if 0 <= nx < N and 0 <= ny < N:
                    if board[nx][ny] == 0:
                        if d == nd: #방향 같으면 코너 x
                            nc = c + 100
                        else: #방향 다르면 코너 o
                            nc = c + 600
                        
                        if nc < price[nx][ny]:
                            price[nx][ny] = nc
                            queue.append([nx, ny, nc, nd])
        
        return price[-1][-1]
    
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1] #서 동 북 남

    return min(bfs(1), bfs(3))

#1. 시작 지점에서 남쪽과 동쪽으로 진행가능
#2. 따라서 남쪽으로 bfs, 동쪽으로 bfs 결과를 함께 비교하여 최소값 도출
#3. bfs + DP 느낌의 문제
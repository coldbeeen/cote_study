#약 63분 소요

from collections import deque

def solution(board):
    def bfs(dir):
        visited = [[False] * n for _ in range(n)]
        price = [[INF] * n for _ in range(n)]
        
        queue = deque([(0, 0, 0, dir)]) #x, y, 비용, 방향
        
        while queue:
            x, y, c, d = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                nc = c
                nd = i #나아갈 방향
                
                if 0 <= nx < n and 0 <= ny < n:
                    if not board[nx][ny]: #벽 아님
                        if nd == d: #직선
                            nc += 100
                        else: #코너
                            nc += 600
                            
                        if nc < price[nx][ny]: #해당 지점 최소 비용 갱신
                            price[nx][ny] = nc
                            queue.append((nx, ny, nc, nd))
                            
        return price[n - 1][n - 1]
                
    
    answer = 0
    
    n = len(board) #정사각형
    
    INF = 1e9
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    return min(bfs(1), bfs(3))

#그래프, 간선 가중치 x -> bfs 문제
#시작 위치는 (0, 0)으로 고정, 도착 지점도 우측 아래로 고정
#직선도로 1개 100원, 코너 500원 추가
#값이 1이면 벽, 0일 때만 지나갈 수 있음
#최소 비용 어떻게 구함? -> board와 shape이 같되, 큰 값으로 초기화된 price 배열 사용 + 순회하며 값 갱신
#코너인지 어떻게 구분? -> 방향도 좌표 리스트와 함께 queue에 저장 + queue에서 pop한 좌표와 현재 좌표 다르면 코너
#방향도 queue에 넣어주기 때문에, 초기에 아무 방향을 넣었었는데 시작점에서 진행하는 방향에 따라 반환값이 달라짐
#왼쪽 상단에서 출발하므로 오른쪽과 아래로 진행하는 케이스 중 더 작은 반환값을 정답으로 return

#방향도 queue에 넣음으로써 코너를 구현하는 아이디어가 있다면 좀 더 쉽게 다가왔을 문제
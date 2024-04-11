import sys
from collections import deque

input = sys.stdin.readline

def check():
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0:
                return True
                
    return False

def bfs():
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if tomato[nx][ny] == 0:
                    tomato[nx][ny] = tomato[x][y] + 1 #익히는 데 걸리는 시간 갱신
                    #원래 익어있던 토마토가 1이므로 걸리는 일수보다 1 큰 값이 저장됨
                    
                    queue.append([nx, ny])

def check_tomato():
    result = 0
    
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0:
                return -1
            
            result = max(result, tomato[i][j])
    
    return result - 1 #1을 빼주는 것에 유의

M, N = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(N)]

queue = deque([])

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i, j]) #처음부터 익어있는 토마토의 인덱스

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] #서 동 남 북

if check():
    bfs()

    print(check_tomato())
else:
    print(0) #저장될 때부터 모든 토마토가 익어 있는 경우

#bfs
#매번 방문 처리 배열을 초기화하면 시간 초과 발생
#deque 모듈 사용 안 하면 시간 초과 발생
#deque 모듈의 popleft 시간 복잡도 : O(1)
#그냥 pop(0) 시간 복잡도 : O(n)

#처음에는 반복적으로 BFS을 실행하면서 토마토가 익는 데 걸리는 시간을 최소로 갱신해가는 로직을 사용함
#이러면 시간 초과 문제를 해결할 수 없음

#생각해보니,
#처음부터 익어있는 토마토의 인덱스를 큐에 다 넣어놓으면 됨
#BFS 로직 상 안 익은 토마토의 값이 알아서 최소값으로 갱신되기 때문
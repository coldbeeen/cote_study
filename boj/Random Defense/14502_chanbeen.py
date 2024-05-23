import sys
import copy
from collections import deque

input = sys.stdin.readline

def install_wall(cnt): #재귀아니면 6중 반복문인데 6중 반복문은 아닌 것 같아서 재귀 함수 생성
    if cnt == 3: #벽 3개 설치 완료하면 바이러스 퍼뜨리기
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1 #벽 설치
                install_wall(cnt + 1) #재귀 호출을 통해 벽 설치하는 모든 경우의 수 살피기
                lab[i][j] = 0 #다음 경우의 수 살펴보기 위해 다시 복원

def bfs():
    global result
    
    queue = deque()
    
    bfs_lab = copy.deepcopy(lab) #벽을 3개 세울때마다 bfs를 순회하므로 복사를 해서 원본 행렬 값 보존
    #그냥 copy로 하면 얕은 복사라서 안 되는 것 같다.. deepcopy 모듈로 깊은 복사를 해줘야 독립적인 행렬이 생성된다
    
    for i in range(N):
        for j in range(M):
            if bfs_lab[i][j] == 2:
                queue.append([i, j]) #바이러스 존재하는 인덱스를 큐에 삽입
    
    while queue: #바이러스 퍼뜨리기
        pop_x, pop_y = queue.popleft()
        
        for i in range(4):
            nx = pop_x + dx[i]
            ny = pop_y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if bfs_lab[nx][ny] == 0:
                    bfs_lab[nx][ny] = 2
                    queue.append([nx, ny])
    
    #안전 구역 개수 카운트, 최댓값 갱신
    cnt = 0
    for i in range(N):
        for j in range(M):
            if bfs_lab[i][j] == 0:
                cnt += 1
    
    result = max(result, cnt)

N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] #서 동 남 북

result = 0

#벽 3개 설치 후, 바이러스 퍼뜨리기
install_wall(0)

print(result)

#깊이 우선 탐색? 너비 우선 탐색?
#너비 우선 탐색으로 작성
#1. 벽 설치
#2. 벽 3개 되면 bfs로 바이러스 퍼뜨리기
#3. 퍼뜨린 후 안전 구역 카운트하여 최댓값 갱신
#1 ~ 3을 모든 벽 설치의 경우의 수에 대해서 반복하기

#deepcopy 구글링해서 찾았음

#3개의 벽을 설치할 때 모든 포인트를 다 돌아야하기 때문에, 좀 비효율적이다
#Python3 시간 초과, Pypy3 통과
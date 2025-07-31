# 아기상어2
# 54분
"""
대각선 방향으로 이동 가능한것이 조금 특이
간단한 BFS 문제인줄 알았는데 그게 아니었다.
오히려 BFS의 특징을 활용해야만 쉽게 풀 수 있는 문제인듯 싶음

1. 초기에는 "상어들의 위치를 찾을때 마다" BFS를 실행 후, visited(distance)배열을 반환
2. 각 상어별로 안전거리들이 나올 것
3. 상어별로 안전거리의 최댓값을 구한 후, 상어들끼리 비교하여 최솟값을 구함

의 흐름으로 가려했는데, 시공간적 복잡도가 너무 클것 같더라


BFS의 특징은 너비우선 탐색이니 당연하게도 근처부터 탐색함
추가로, 상어(1)의 위치부터 탐색하기에 방문처리배열도 필요가 없이 기존배열에다가 실행하면 됨
따라서,

1. 처음에 상어들의 위치를 큐에 append 후 BFS를 1번만 실행하게 된다면,
2. 각 상어별로 한칸씩 탐색을 진행하다가 어느순간 중간지점(?) 에서 마주치게 될것
3. 그 이후로는 탐색을 더한다면 다른 상어들의 최소 안전거리를 침해하게 될테니 바로 종료해도 됨

"""


import sys
from collections import deque

input=sys.stdin.readline
def bfs():
    # visited=[[0]*m for _ in range(n)]
    # q=deque()
    # q.append((x,y))
    # visited[x][y]=0
    
    while q:
        cx,cy=q.popleft()
        for i in range(8):
            nx=cx+dx[i]
            ny=cy+dy[i]
            
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
                graph[nx][ny]=graph[cx][cy]+1
                q.append((nx,ny))
    return 

# 대각선 방향까지 8방향 고려
dx=[1,-1,0,0,1,1,-1,-1]
dy=[0,0,1,-1,1,-1,-1,1]

n,m=map(int,input().split())

graph=[list(map(int,input().split())) for _ in range(n)]
q=deque()
total=0

# 상어들의 위치부터 찾아서 q에 넣어줌
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            q.append((i,j))

bfs()

# 최종 안전거리들의 최댓값 구함
for i in range(n):
    total=max(total,max(graph[i]))
# 이때, 상어(1)부터 시작했으니 거리는 -1
print(total-1)

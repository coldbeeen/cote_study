import sys
from collections import deque
input=sys.stdin.readline


m,n=map(int,input().split())
graph=[]
q=deque()
dx=[-1,1,0,0]
dy=[0,0,-1,1]
total=float("-inf")

#BFS로도 dx dy를 써보는게 처음이라 생각을 못했네...당연히 사용할 수 있는건데
#약간의 구글링을 하였음
def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                q.append([nx, ny])

for _ in range(n):
    tomato = list(map(int, input().split()))
    graph.append(tomato)

# 성우한테 힌트얻음(처음에 1인애들을 다 넣어놓고 BFS시작)
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            q.append([j,i])

bfs()
for row in graph:
    tmp=0
    if 0 in row:
        total=-1
        break
    tmp=max(row)
    total=max(tmp,total)

print(total-1 if total!=-1 else -1)

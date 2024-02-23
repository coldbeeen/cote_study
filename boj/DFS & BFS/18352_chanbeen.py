import sys
from collections import deque

input = sys.stdin.readline

def BFS(v):
    queue = deque([v])
    
    visited[v] = 0 #방문 처리
    
    while queue:
        pop = queue.popleft()
        
        for n in graph[pop]:
            if visited[n] == -1:
                visited[n] = visited[pop] + 1 #최단거리 갱신
                queue.append(n)

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    
    graph[s].append(e) #단방향

visited = [-1] * (N + 1)

BFS(X)

flag = 0

for i in range(1, N + 1):
    if visited[i] == K:
        print(i)
        flag = 1

if not flag:
    print(-1)
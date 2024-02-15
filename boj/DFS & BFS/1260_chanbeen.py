import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    
    graph[s].append(e)
    graph[e].append(s)

for i in range(N + 1): #그래프 내 요소 작은 순 정렬
    graph[i].sort()

def DFS(v):
    print(v, end=' ')
    visited[v] = 1
    
    for n in graph[v]:
        if visited[n] == 0:
            DFS(n)
            
def BFS(v):
    queue = deque([v])
    
    visited[v] = 1
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for n in graph[v]:
            if visited[n] == 0:
                queue.append(n)
                visited[n] = 1

visited = [0] * (N + 1)
DFS(V)

print()

visited = [0] * (N + 1)
BFS(V)

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def DFS(v):
    visited[v] = 1
    
    for n in graph[v]:
        if visited[n] == 0:
            DFS(n)

cnt = 0
visited = [0] * (N + 1)

for i in range (1, N + 1):
    if visited[i] == 0:
        DFS(i)
        cnt += 1

print(cnt)
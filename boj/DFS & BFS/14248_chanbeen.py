def DFS(v):
    global cnt
    
    if visited[v] == 0:
        cnt += 1 #새롭게 방문하는 돌
    
    visited[v] = 1
    
    left = v - graph[v]
    right = v + graph[v] #좌우로 이동가능
    
    if 0 < left <= n and visited[left] == 0:
        DFS(left)
    if 0 < right <= n and visited[right] == 0:
        DFS(right)

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

graph = []
graph.append(0)

jump = list(map(int, input().split()))

for i in range(len(jump)):
    graph.append(jump[i])

visited = [0] * (n + 1)

cnt = 0

start = int(input())
DFS(start)

print(cnt)
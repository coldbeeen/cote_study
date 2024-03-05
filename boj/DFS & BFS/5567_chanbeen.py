import sys
from collections import deque

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    queue += graph[1] #친구의 친구까지만 탐색
    
    while queue:
        pop = queue.popleft()
        
        for n in graph[pop]:
            if not visited[n]:
                visited[n] = True

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a) #양방향 연결
    
visited = [False for _ in range(n + 1)]

bfs(1)

visited[1] = False #상근이 본인이므로 방문처리 해제
print(visited.count(True))
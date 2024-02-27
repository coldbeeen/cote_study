import sys
from collections import deque

input = sys.stdin.readline

def BFS(v):
    queue = deque([v])
    
    visited[v] = 0 #방문 처리, 초기 비용
    
    while queue:
        pop = queue.popleft()
        
        for n in graph[pop]:
            if visited[n] == -1:
                visited[n] = visited[pop] + 1 #비용 갱신
                queue.append(n)

a, b = map(int, input().split())

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    
    graph[s].append(e)
    graph[e].append(s) #단뱡향인줄 알았지만, 예시보니 양방향

visited = [-1] * (N + 1)

BFS(a)

print(visited[b]) #도착지점으로 가는데 드는 최소비용
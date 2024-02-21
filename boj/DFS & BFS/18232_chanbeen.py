#구글링
def BFS(v):
    queue = deque([v])
    
    visited[v] = 0 #방문 처리, 시간 초기값 0
    
    while queue:
        pop = queue.popleft()
        
        nodes = [] # 인접 리스트
        nodes += [pop - 1, pop + 1] # X-1, X+1
        
        if graph[pop]:
            nodes += graph[pop] # 연결된 지점
        
        for n in nodes:
            if 1 <= n <= N:
                if visited[n] == -1:
                    queue.append(n)
                    visited[n] = visited[pop] + 1 # 소요 시간 갱신
            
            if n == E:
                return visited[n] # 목적지로 가는데 걸리는 시간

import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
S, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    
    graph[y].append(x) #양방향 연결
    graph[x].append(y)

visited = [-1] * (N + 1) #방문처리 및 비용관리를 위해 -1로 초기화

print(BFS(S))

#DFS로는 계속 시간초과 뜨네..
#BFS로 푸는 방법은 아직 익숙치 않아서 구글링했음
#DFS로 풀기 편한 문제랑 BFS로 풀기 편한 문제를 어떻게 구별하지?
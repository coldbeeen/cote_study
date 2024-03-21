import sys

input = sys.stdin.readline

n = int(input())
idx1, idx2 = map(int, input().split())

m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    
    graph[s].append(e)
    graph[e].append(s) #양방향 연결

def DFS(v, num):
    global result
    num += 1 #촌수 계산
    visited[v] = 1 #방문 처리
    
    if v == idx2:
        result = num
    
    for n in graph[v]:
        if visited[n] == 0:
            DFS(n, num)

result = 0
visited = [0] * (n + 1)

DFS(idx1, 0)

print(result - 1 if result != 0 else -1)

#반례
# 3
# 2 3
# 2
# 1 2
# 2 3
# 2와 3은 1촌 관계지만 visited가 들어가면서 처리되어버려서 2촌 관계로 출력됨
# 죄다 방문처리하면서 visited.count(1)로 해버리니까 1, 2, 3중에 1도 집계되어버려서 그럼
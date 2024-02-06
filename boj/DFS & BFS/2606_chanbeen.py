import sys

input = sys.stdin.readline

N = int(input())
E = int(input())
graph = [[] for _ in range(N + 1)]

for i in range(1, E+1):
    s, e = map(int, input().split())
    
    graph[s].append(e)
    graph[e].append(s) #양방향 연결, 인접 노드들을 2차원 리스트에 담아줌

def DFS(v):
    visited[v] = 1
    
    for e in graph[v]:
        if visited[e] == 0:
            DFS(e)

visited = [0] * (N + 1)

DFS(1)

print(visited.count(1) - 1) #1은 처음부터 감염되었으므로 하나 제외

#처음에 노드에 엣지 연결할 때 양방향 연결을 해줘야 반례 케이스를 해결할 수 있다.
#반례, 부분적 연결 형성하다가 마지막에 전체적으로 연결되는 케이스 
#6
#5
#1 2
#2 5
#3 4
#4 6
#5 6
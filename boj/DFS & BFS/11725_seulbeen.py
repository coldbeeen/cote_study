#visit체크하는 배열에 부모노드를 담아주면 됨 그냥
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1): 
    x, y = map(int, input().split())  
    graph[x].append(y)
    graph[y].append(x)
parent=[False for _ in range(n+1)]#부모노드 담을 배열 겸 방문체크배열

def dfs(idx):
    for i in graph[idx]:
        if parent[i]==False:
            parent[i] = idx
            dfs(i) 

dfs(1) 

for i in range(2, n+1):
    print(parent[i])
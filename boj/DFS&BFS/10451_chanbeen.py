#기존으로 하면 Recursion Error
import sys
sys.setrecursionlimit(2000) #기존에는 1000

input = sys.stdin.readline

def DFS(v):
    global cnt
    if visited[v] == 1: #싸이클 형성
        cnt += 1
        return
    
    for n in graph[v]:
        if visited[n] != -1: #사용 가능한 노드만
            visited[v] = 1
            DFS(n)
        visited[n] = -1 #이미 싸이클 형성에 사용된 노드는 재사용 불가 처리

for _ in range(int(input())):
    N = int(input())
    array = list(map(int, input().split()))
    
    graph = [[] for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        graph[i].append(array[i - 1])
    
    cnt = 0
    visited = [0] * (N + 1)
    
    for i in range(N):
        if visited[i + 1] != -1: #아직 방문 안 한 노드만 싸이클 형성 여부 판별
            DFS(array[i])
    
    print(cnt)
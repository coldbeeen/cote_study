import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def search_tree(v):  # DFS로 트리를 탐색함
    visited[v] = True  # 방문 처리

    for i in graph[v]:  # 연결되어 있는 정점 순회
        if not visited[i]:  # 방문하지 않은 정점이라면
            result[i] = v  # 해당 정점의 부모를 저장
            search_tree(i)  # DFS 재귀

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):  # 인접리스트 방식 저장
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False for _ in range(n+1)]
result = [0 for _ in range(n+1)]  # 각 정점의 부모를 담는 리스트

search_tree(1)  # 부모부터 DFS 수행
for i in range(2, n+1):  # 2번 정점부터 부모 출력
    print(result[i])
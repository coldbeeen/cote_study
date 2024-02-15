import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)  # 재귀 최대 깊이 설정

n, m = map(int, input().split())


graph = [[] for _ in range(n+1)]  # 인접리스트 방식으로 그래프 표현

def search(v):  # DFS 수행 함수
    visited[v] = True  # 방문 처리

    for i in graph[v]:  # 인접 정점 순회
        if not visited[i]:  # 방문되지 않은 정점이라면
            search(i)  # 재귀

for _ in range(m):  # 간선 입력
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(n+1)]  # 방문 여부를 표현하기 위한 리스트
result = 0

for i in range(1, n+1):  # 1~n 까지의 정점 순회
    if not visited[i]:  # 방문하지 않은 정점이라면 DFS 수행
        search(i)
        result += 1

print(result)
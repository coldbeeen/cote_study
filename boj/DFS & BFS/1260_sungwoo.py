from collections import deque

def DFS(v):
    print(v, end=' ')
    visited[v] = True  # 방문 처리

    for i in sorted(graph[v]):  # 번호가 낮은 정점부터 방문
        if not visited[i]:  # 방문한 곳이 아니라면 DFS 재귀
            DFS(i)

def BFS(v):
    queue = deque()  # deque를 통해 큐 구현
    queue.append(v)  # 시작 정점 v부터 시작
    visited[v] = True  # 시작 정점 방문 처리

    while queue:  # 큐가 빌 때까지 반복
        v = queue.popleft()
        print(v, end=' ')

        for i in sorted(graph[v]):  # 번호가 낮은 정점부터 방문
            if not visited[i]:  # 방문한 곳이 아니라면 큐에 추가한 뒤 방문 처리
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):  # 인접 리스트 방식으로 그래프 구현
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# DFS 탐색 수행
visited = [False for i in range(n+1)]
DFS(v)
print()

# BFS 탐색 수행
visited = [False for i in range(n+1)]
BFS(v)
from collections import deque

def solution(n, roads, sources, destination):

    graph = [[] for _ in range(n + 1)]  # 인접리스트 생성
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    q = deque([destination])  # destination을 출발점으로하여 sources까지의 거리를 계산할 것임
    visited = [False for _ in range(n+1)]
    distance = [-1 for _ in range(n+1)]

    visited[destination], distance[destination] = True, 0  # 출발점 방문 처리 및 거리 초기화

    while q:  # BFS 수행
        v = q.popleft()

        for i in graph[v]:  # 방문하지 않은 인접한 지역 순회
            if not visited[i]:
                q.append(i)
                visited[i] = True
                distance[i] = distance[v] + 1

    answer = []
    for source in sources:  # 각 source까지의 거리로 answer 구함
        answer.append(distance[source])

    return answer
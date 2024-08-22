from collections import deque

def solution(n, edge):
    answer = 0

    # edge를 인접 리스트 형태 변환
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)

    # 거리를 구하기 위해 BFS 수행
    # 큐와 거리(방문 여부) 리스트 생성
    q = deque([1])
    distances = [-1 for _ in range(n + 1)]
    distances[1] = 0  # 시작 노드의 거리 0으로 설정

    # BFS 수행
    while q:

        v = q.popleft()

        for i in graph[v]:  # 연결된 모든 노드 순회
            if distances[i] == -1:  # 거리가 -1(방문 X)이라면 큐에 추가하고 거리 설정
                q.append(i)
                distances[i] = distances[v] + 1

    return distances.count(max(distances))  # 가장 멀리 떨어진 노드 개수 리턴
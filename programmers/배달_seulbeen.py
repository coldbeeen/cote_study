# 1833
# 플로이드워셜 알고리즘
# 다익스트라처럼 한 정점에서 다른 정점까지의 최단 거리를 갱신하는 알고리즘
def solution(N, road, K):
    INF = 500000
    answer = 0
    graph = [[INF] * (N + 1) for i in range(N + 1)]
    # 자기 자신(주대각성분)은 0
    for i in range(N + 1):
        graph[i][i] = 0

    # 그래프 초기화(간선 정보대로)
    for r in road:
        graph[r[0]][r[1]] = min(graph[r[0]][r[1]], r[2])
        graph[r[1]][r[0]] = min(graph[r[0]][r[1]], r[2])

    # a->b로 가는 정점중, x노드를 거쳐 가는 정점들과 거리 비교 후 갱신
    for x in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                # a->x + x->b 와의 거리 비교
                graph[a][b] = min(graph[a][b], graph[a][x] + graph[x][b])
    
    # 이거는 그래프 출력용(필요없음)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(graph[i][j], end=" ")
        print()
    
    # 문제의 조건이 1번노드 출발이므로, graph[1](1번노드 ~ 각 노드까지 가는 최단거리를 담은 배열)에서 K보다 작거나 같은 원소의 개수를 구하면 됨
    answer = len([d for d in graph[1] if d <= K])
    return answer

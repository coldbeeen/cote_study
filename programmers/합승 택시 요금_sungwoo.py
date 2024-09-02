def solution(n, s, a, b, fares):

    def get_smallest_node(costs, visited):  # 아직 방문하지 않은, 가장 비용이 작은 노드를 리턴

        min_cost, min_node = (INF, -1)
        for i in range(1, n+1):
            if costs[i] < min_cost and not visited[i]:
                min_cost, min_node = costs[i], i

        return min_node

    def dijkstra(s):  # 다익스트라 알고리즘 수행 (비용 리스트 리턴)

        costs = [INF for _ in range(n + 1)]
        visited = [False for _ in range(n + 1)]

        for i in range(1, n + 1):  # 시작 노드와 연결되어 있는 노드 비용 초기화
            costs[i] = cost_matrix[s][i]

        visited[s] = True  # 시작노드 방문 처리

        for _ in range(n-1):  # 출발점을 제외한 노드 수는 n-1개이므로, 최대 n-1번 수행
            node = get_smallest_node(costs, visited)  # 비용가 구해진 노드 중 가장 최소 비용인 노드 선택
            visited[node] = True

            for i in range(1, n+1):  # 모든 노드를 순회하며, 기존 비용보다 더 적은 비용이 계산될 경우 갱신
                if not visited[i] and costs[node] + cost_matrix[node][i] < costs[i]:
                    costs[i] = costs[node] + cost_matrix[node][i]

        return costs

    INF = float('inf')

    # 0. 비용 행렬 생성
    cost_matrix = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        cost_matrix[i][i] = 0
    for i, j, k in fares:
        cost_matrix[i][j] = cost_matrix[j][i] = k

    # 1. '중간 지점까지의 최소 비용'를 구함
    mid_costs = dijkstra(s)

    # 2. 중간 지점을 바꿔가며, '중간 지점부터 a, b까지의 최소 비용'를 구함
    final_cost = INF
    for i in range(1, n+1):
        costs = dijkstra(i)
        final_cost = min(final_cost, mid_costs[i] + costs[a] + costs[b])

    return final_cost
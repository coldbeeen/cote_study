# 54분
# 변수 명이 겹쳐서오류가 났는데 디버깅하는데 오래걸렸음... 앞으로 주의하자
# 이거야말로 플로이드워셜?
def solution(n, s, a, b, fares):
    
    # 문제 조건의 최댓값
    INF = 100000

    # 그래프 작업
    graph = [[INF * (n - 1)] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i][i] = 0
    for f in fares:
        start, end, fare = f[0], f[1], f[2]
        graph[start][end] = min(fare, graph[start][end])
        graph[end][start] = min(fare, graph[end][start])
    
    #플로이드워셜 알고리즘 수행
    # a->b의 경로들에서, x노드를 거쳐가는 경우들 탐색 후 갱신
    for x in range(1, n + 1):
        for A in range(1, n + 1):
            for B in range(1, n + 1):
                graph[A][B] = min(graph[A][B], graph[A][x] + graph[x][B])
    # 이러면, 정확히 어느 노드들을 거쳐서 간건진 모르지만, 아무튼 a->b 까지의 최적최단의 거리가 배열에 담기게되겠지?


    # S->a, S->b까지 가는데, 어느 노드까지 합승하고, 어느노드까지 따로 갈것이냐?
    
    # 합승을 아예 안하는게 최고 택시요금
    answer = graph[s][a] + graph[s][b]

    # s->i 까지 합승 + i->a 까지 각자 + i->b 까지 각자
    for i in range(1, n + 1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
    return answer

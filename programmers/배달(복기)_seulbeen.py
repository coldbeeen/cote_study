# 시간 얼마 걸렸는지 모르겠음,,, 그냥 될때까지 풀어봄
# 플로이드 워셜은 각 지점에서 다른 지점들까지의 최단거리
# 다익스트라는 한 지점에서 다른 지점들까지의 최단거리
# 다익스트라로 ㄱㄱ
import heapq


def solution(N, road, K):
    #문제에서 주어진 거리의 최댓값
    INF = 500000

    #1번노드에서 각 노드까지의 거리를 담는 배열, 초기는 INF
    distance = [0 if i == 1 else INF for i in range(N + 1)]
    
    graph = [[] for _ in range(N + 1)]
    
    for r in road:
        # (도착노드,연결거리)
        graph[r[0]].append((r[1], r[2]))
        graph[r[1]].append((r[0], r[2]))
    print(graph)
    q = []
    heapq.heappush(q, (0, 1))

    # print(q)
    while q:
        #(거리와 노드)를 pop
        weight, node = heapq.heappop(q)

        # 현재 탐색한 노드의 거리가 '거리 배열' 값보다 작을때 (크다면, 이미 최솟값이 갱신된거니까)
        if weight <= distance[node]:

            # 현재 노드에 연결된 다른 노드 검색
            for i in graph[node]:
                # 거리비교
                if distance[i[0]] > weight + i[1]:
                    distance[i[0]] = weight + i[1]
                    heapq.heappush(q, (weight + i[1], i[0]))
    print(distance)

    answer = len([d for d in distance if d <= K])
    return answer

#구글링

import heapq

def solution(n, s, a, b, fares):
    def dijkstra(start):
        # 최단 거리 테이블을 무한대로 초기화
        distances = [float('inf')] * (n + 1)
        distances[start] = 0  # 시작 노드까지의 거리는 0

        # 우선순위 큐(힙)을 사용하여 처리할 노드 관리
        queue = [(0, start)]  # (거리, 노드)

        while queue:
            # 가장 거리가 짧은 노드를 꺼낸다
            current_distance, current_node = heapq.heappop(queue)

            # 이미 처리된 노드면 무시
            if current_distance > distances[current_node]:
                continue

            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight

                # 더 짧은 경로를 발견한 경우
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

        return distances
                
    answer = float('inf')
    
    graph = [[] for _ in range(n + 1)]
    
    for i in range(len(fares)):
        u, v, c = fares[i]
        
        graph[u].append([v, c])
        graph[v].append([u, c]) #양방향 연결
    
    # i번째 노드에서 각 노드로 갈 때 최소 비용이 담긴 배열 생성
    D = [0] + [dijkstra(i) for i in range(1, n + 1)]
    
    for i in range(1, n + 1):
        answer = min(answer, D[s][i] + D[i][a] + D[i][b]) #s와 i가 같으면 합승을 안 한 경우, s와 i가 다르면 s부터 i까지 합승을 한 경우
    
    return answer

# dfs로 해결하는 문제인 줄 알았지만..
# 구글링 결과 다익스트라 알고리즘을 활용한 최단 경로 문제라고 함


# 다익스트라 알고리즘에서 heapq 자료구조를 사용하는 이유
# 1. 아직 방문하지 않은 노드 중 가장 적은 비용을 가진 노드를 pop하여 최적 비용 계산을 빠르게 하기 위해서
# 2. 비용 갱신 후 삽입, 삭제 작업 반복 시 기존 리스트에서는 O(n)이 걸리지만 heapq 사용 시 O(log n)에 해결 가능
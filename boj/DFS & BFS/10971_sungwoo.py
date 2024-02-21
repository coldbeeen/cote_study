def find_ways(cur_city, cur_cost):  # 백트래킹을 활용해 모든 경로 탐색
    global start_city, min_cost  # 시작 도시와 최단 비용

    if all(visited):  # 모두 방문했다면 (재귀 종료 조건)
        if graph[cur_city][start_city] != 0:  # 시작 도시로 갈 수 있는지 확인한 후
            final_cost = cur_cost + graph[cur_city][start_city]
            min_cost = min(min_cost, final_cost)  # min_cost 업데이트
        return

    for next_city in range(n):  # 모든 도시 순회
        if (not visited[next_city]  # 방문하지 않은 도시고
                and graph[cur_city][next_city] != 0  # 갈 수 있는 도시이며
                and cur_cost + graph[cur_city][next_city] < min_cost):  # 갔을 때 비용이 min_cost를 넘지 않는다면 (다른 코드 참고)
            visited[next_city] = True
            next_cost = cur_cost + graph[cur_city][next_city]  # 현재 비용을 업데이트한 후
            find_ways(next_city, next_cost)  # 다음 도시로 이동 (재귀)
            visited[next_city] = False


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [False for _ in range(n)]
min_cost = float('inf')

for start_city in range(n):  # 시작 도시 1~N 순회
    visited[start_city] = True
    find_ways(start_city, 0)  # 백트래킹 함수 진입
    visited[start_city] = False

print(min_cost)  # 최단 비용 출력
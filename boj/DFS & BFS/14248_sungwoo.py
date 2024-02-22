def search_stones(v):  # 돌 탐색을 위해 DFS 수행
    visited[v] = True   # 방문 처리

    nx_list = [v - stones[v], v + stones[v]]  # 왼쪽 / 오른쪽 점프 후 위치

    for nx in nx_list:
        if 0 <= nx < n and not visited[nx]:  # 유효한 위치이고 방문하지 않았다면
            search_stones(nx)  # DFS 재귀




n = int(input())
stones = list(map(int, input().split()))
start = int(input()) - 1

visited = [False for i in range(n + 1)]  # 방문 처리를 위한 리스트
search_stones(start)
print(sum(visited))  # visited 리스트를 통해 방문가능한 돌의 개수 출력
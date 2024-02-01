T = int(input())

for t in range(T):

    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False for i in range(n+1)]  # 방문 여부
    result = 0

    for i in range(1, n+1):  # 순열을 순회
        if visited[i]:  # 방문한 정점일 경우 이미 사이클을 세었으므로 continue
            continue

        v = i
        while not visited[v]:  # 방문하지 않은 정점일동안 반복 (사이클 순회)
            visited[v] = True  # 방문 처리
            v = graph[v]  # 다음 정점으로

        result += 1  # 반복문이 끝난 경우 사이클 하나를 순회한 것임

    print(result)
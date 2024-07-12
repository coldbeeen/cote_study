def dfs(computers, node, visited):

    # 노드 방문 처리
    visited[node] = True

    # 노드 순회하며, 연결되어 있고 방문하지 않은 노드에 대해 dfs 재귀
    for i in range(len(computers)):
        if computers[node][i] and not visited[i]:
            dfs(computers, i, visited)

def solution(n, computers):

    answer = 0
    visited = [False for _ in range(n)]  # 방문 여부 관리

    # 모든 노드에 대해 순회하며, 방문하지 않은 노드에 대해 dfs 실행
    for i in range(n):
        if not visited[i]:
            dfs(computers, i, visited)
            answer += 1  # dfs가 끝난 후 네트워크 개수 1 증가함

    return answer

a = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(3, a))
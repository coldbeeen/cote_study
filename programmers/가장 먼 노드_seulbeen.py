from collections import deque

def solution(n, edge):
    
    graph = [[] for _ in range(n + 1)]
    visit = [False for _ in range(n + 1)]
    depth = [0 for _ in range(n + 1)]

    #양방향 그래프 구축
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    # BFS
    q = deque()
    q.append(1)
    visit[1] = True

    while q:
        node = q.popleft()

        for n in graph[node]:
            if not visit[n]:
                visit[n] = True
                depth[n] = depth[node] + 1
                q.append(n)

    #가장 먼 노드의 길이 구함
    m_depth = max(depth)
    
    #가장 먼 노드의 개수 구함
    cnt = 0
    for d in depth:
        if d == m_depth:
            cnt += 1
    return cnt

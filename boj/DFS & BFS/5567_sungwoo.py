from collections import deque

n, m = [int(input()) for _ in range(2)]
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]  # 같은 관계를 반복해서 탐색하지 않도록 방문 처리
distance = [-1 for _ in range(n+1)]  # 거리
for _ in range(m):  # 인접리스트 방식 표현
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

q = deque([1])  # 상근이부터 시작
visited[1] = True
distance[1] = 0

while q:  # BFS 수행
    v = q.popleft()
    if distance[v] > 2:  # 친구의 친구까지만 초대하므로 2보다 크면 break
        break

    for i in graph[v]:
        if not visited[i]:
            q.append(i)
            visited[i] = True  # 방문 처리
            distance[i] = distance[v] + 1  # 친구 관계 1 증가

result = len([dist for dist in distance if 1 <= dist <= 2])  # distance가 1 이상 2 이하인 요소 개수
print(result)
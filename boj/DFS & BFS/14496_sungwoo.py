from collections import deque

a, b = map(int, input().split())
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]  # 무한 치환이 일어날 수 있기 때문에 방문 처리 필요
distance = [-1 for _ in range(n+1)]  # 거리
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

q = deque([a])
visited[a] = True
distance[a] = 0

while q:  # BFS 수행
    v = q.popleft()

    for i in graph[v]:
        if not visited[i]:
            distance[i] = distance[v] + 1  # 치환 횟수 증가
            visited[i] = True  # 방문 처리
            if i == b:  # 찾고자 하는 문자라면 break
                break
            q.append(i)
    else:
        continue  # 위 for문에서 break 만나지 않은 경우 while문 반복
    break  # break 만난 경우 더 이상 진행할 필요가 없으므로 종료

print(distance[b] if distance[b] != -1 else -1)  # distance가 0 이상이 아니라면 -1 출력
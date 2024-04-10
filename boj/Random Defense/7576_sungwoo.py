from collections import deque

m, n = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(n)]
q = deque()

for x in range(n):  # 가장 먼저 익은 토마토를 큐에 추가!
    for y in range(m):
        if tomatoes[x][y] == 1:
            q.append((x, y))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
result = 1

while q:  # BFS 수행!
    x, y = q.popleft()

    for i in range(4):  # 상하좌우 순회
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and tomatoes[nx][ny] == 0:  # 유효한 위치이고, 안 익은 토마토라면 큐에 추가!
            result = tomatoes[nx][ny] = tomatoes[x][y] + 1  # 1 이상의 값은 '익은 토마토의 익는 데 걸린 일수 + 1'로 간주하여 풀이 (가장 마지막에 저장된 값이 result)
            q.append((nx, ny))

for tomato in tomatoes:  # 0(안 익은 토마토)이 하나라도 있다면 -1 출력
    if 0 in tomato:
        print(-1)
        break
else:
    print(result - 1)
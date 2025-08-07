#80분 +@, 구글링

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

shark = deque()
for i in range(n):
    temp = list(map(int, input().split()))
    for t in range(m):
        if temp[t] == 1:
            shark.append((i, t)) #상어 위치를 처음에 담아놓고 bfs를 한번만 실행
    arr.append(temp)

mx = [-1, -1, -1, 0, 1, 0, 1, 1]
my = [-1, 0, 1, 1, 1, -1, 0, -1]


def bfs():
    while shark:
        x, y = shark.popleft()
        for k in range(8):
            dx = x + mx[k]
            dy = y + my[k]
            if 0 <= dx < n and 0 <= dy < m:
                if arr[dx][dy] == 0:
                    shark.append((dx, dy))
                    arr[dx][dy] = arr[x][y] + 1
    return


bfs()
safe_dist = 0
for i in range(n):
    for j in range(m):
        safe_dist = max(safe_dist, arr[i][j])

print(safe_dist - 1)

#상어 위치를 기준으로 bfs를 진행하는 것이 포인트
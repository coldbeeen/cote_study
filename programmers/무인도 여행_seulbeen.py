#34분
from collections import deque


def solution(maps):
    answer = []
    # bfs를 위한 visit배열과 dx,dy
    visit = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visit[x][y] = True
        food = int(maps[x][y])
        while q:
            x, y = q.popleft()
            for i in range(4):
                cx = x + dx[i]
                cy = y + dy[i]
                if (
                    0 <= cx < len(maps)
                    and 0 <= cy < len(maps[0])
                    and visit[cx][cy] == False
                    and maps[cx][cy] != "X"
                ):
                    visit[cx][cy] = True
                    food += int(maps[cx][cy])
                    q.append((cx, cy))
        return food

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            # 방문을 하지 않은 섬에 대하여 bfs 진행
            if not visit[i][j] and maps[i][j] != "X":
                answer.append(bfs(i, j))
    if not answer:
        return [-1]
    # 문제 조건에 맞게 정렬 후 return
    answer.sort(reverse=False)
    return answer

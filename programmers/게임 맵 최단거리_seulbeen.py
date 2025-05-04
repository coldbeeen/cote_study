# 29분
"""
최단거리니까 BFS
내 위치 (0,0), 상대 위치 (n-1,m-1)
1이 갈 수 있는 길
"""
from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    q = deque()
    visit = [[False for _ in range(m)] for _ in range(n)]
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    # (행,열,거리)
    q.append((0, 0, 1))
    while q:
        r, c, cnt = q.popleft()

        for i in range(4):
            cr = r + dr[i]
            cc = c + dc[i]
            if 0 <= cr < n and 0 <= cc < m:
                if not visit[cr][cc] and maps[cr][cc] == 1:
                    # 목표에 도달했으면 return
                    if cr == n - 1 and cc == m - 1:
                        return cnt + 1
                    
                    visit[cr][cc] = True
                    q.append((cr, cc, cnt + 1))
    #목표에 도달하지 못했으면(즉, 목표좌표의 visit배열이 False이면) return -1
    if not visit[n - 1][m - 1]:
        return -1

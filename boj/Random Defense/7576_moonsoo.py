import sys
sys.setrecursionlimit(10**6)

def count_fresh():
    global M, N
    cnt = 0

    for row in range(N):
        for col in range(M):
            t = tom[row][col]
            if t == 0:
                cnt += 1

    return cnt

def BFS(ripen):
    global cnt

    if len(ripen) == 0:
        return 
    
    rp2 = []
    for rc in ripen:
        row, col = rc[0], rc[1]
        # print(f"({row},{col})")
        for i in range(4):
            nr, nc = row + dx[i], col + dy[i]
        
            if 0 <= nr < N and 0 <= nc < M and tom[nr][nc] == 0:
                tom[nr][nc] = 1
                rp2.append((nr, nc))
    # print(rp2)
    # print()
    cnt += 1
    BFS(rp2)

M, N = map(int, input().split())

tom = [list(map(int, input().split())) for _ in range(N)]
ripen = []

for row in range(N):
    for col in range(M):
        t = tom[row][col]

        if t == 1:
            cr = (row, col)
            ripen.append(cr)


cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


BFS(ripen)
fresh = count_fresh()

if fresh > 0:
    print(-1)
elif cnt == 1:
    print(0)
else:
    print(cnt - 1)



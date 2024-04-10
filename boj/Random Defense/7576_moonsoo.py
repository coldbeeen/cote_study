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

    # 종료조건
    if len(ripen) == 0:
        return 
    
    rp2 = []
    for rc in ripen:
        row, col = rc[0], rc[1]
        # print(f"({row},{col})")
        for i in range(4):
            # 상하좌우 토마토를 확인하며 익지 않았을 경우 익히고 새로운 ripen리스트에 추가하여 BFS의 인자로 넣어준다
            nr, nc = row + dx[i], col + dy[i]
        
            if 0 <= nr < N and 0 <= nc < M and tom[nr][nc] == 0:
                tom[nr][nc] = 1
                rp2.append((nr, nc))

    # 하루 카운팅
    cnt += 1
    # 오늘 날짜에 대해 익은 토마토의 좌표에 대해서만 새로 BFS를 실행
    BFS(rp2)

M, N = map(int, input().split())

tom = [list(map(int, input().split())) for _ in range(N)]
ripen = []

# 토마토 박스롤 돌면서 익은 상태의 토마토 좌표를 ripen에 저장
for row in range(N):
    for col in range(M):
        t = tom[row][col]

        if t == 1:
            cr = (row, col)
            ripen.append(cr)


cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS를 돌면서 익은 토마토 주변의 안 익은 토마토를 방문과 카운팅
BFS(ripen)

# 모든 BFS가 끝난 후 아직 익지 않은 토마토가 남아있는지 확인
fresh = count_fresh()

if fresh > 0:
    # 익지 않은 토마토가 남아있으면
    print(-1)
elif cnt == 1:
    # 첫날부터 모두 익어있었으면
    print(0)
else:
    # 모든 토마토가 익기까지 걸리는 최소 일수 출력
    print(cnt - 1)



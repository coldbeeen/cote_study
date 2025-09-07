#약 55분 소요

N = int(input())

moves = list(input().rstrip())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1] #북, 동, 남, 서

maps = [['#'] * 101 for _ in range(101)] #입력 최댓값 50, 좌우 여유분 50씩

x, y, d = 50, 50, 2 #시작점, 시작 방향 : 남쪽

ex = ey = sx = sy = 50 #초기 좌표

maps[x][y] = '.' #초기 좌표

for move in moves:
    if move == 'L':
        d = (d + 3) % 4 #방향 갱신 : 왼쪽 90도 회전
    elif move == 'R':
        d = (d + 1) % 4 #방향 갱신 : 오른쪽 90도 회전
    else: #F
        x = x + dx[d]
        y = y + dy[d]

        maps[x][y] = '.'

        ey = max(ey, y) #max 좌표 : 끝 x, y
        ex = max(ex, x)

        sy = min(sy, y) #min 좌표 : 시작 x, y
        sx = min(sx, x)

for i in range(sx, ex + 1):
    for j in range(sy, ey + 1):
        print(maps[i][j], end = '')
    print()
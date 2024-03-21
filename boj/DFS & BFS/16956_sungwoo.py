def fence(x, y):  # 상하좌우 위치에 울타리를 설치하는 함수 (양 위치에서만 실행)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:  # 유효한 위치 검증
            if graph[nx][ny] == '.':  # 빈 곳이라면 울타리 설치
                graph[nx][ny] = 'D'
            elif graph[nx][ny] == 'W':  # 늑대가 붙어있다면 False를 출력하여 더 이상 진행 X
                return False
    return True

r, c = map(int, input().split())

graph = [list(input()) for i in range(r)]
end_flag = False

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':  # 양 일때 울타리 설치
            can_continue = fence(i, j)

            if not can_continue:  # 늑대가 붙어 있었다면 더 이상 진행 X
                end_flag = True
                break
    if end_flag:
        break

if end_flag:  # 양 가두기 실패
    print(0)
else:  # 양 가두기 성공
    print(1)
    for row in graph:
        print(''.join(row))
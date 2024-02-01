import sys
input = sys.stdin.readline

def isValid(x, y):  # 좌표가 유효한지 검사 (나갔는지, 막혔는지, 방문했는지)
    global r, c
    if 0 <= x < r and 0 <= y < c and graph[x][y] == '.' and not visited[x][y]:
        return True
    return False

def backtrack(x, y, distance):
    global r, c, k, result
    if x == 0 and y == c - 1:  # 목적지 도달 시
        if distance == k:  # 거리가 k라면 result 증가
            result += 1
        return

    for i in range(4):  # 위, 아래, 왼쪽, 오른쪽 좌표 시도
        nx = x + dx[i]
        ny = y + dy[i]
        if isValid(nx, ny):  # 좌표가 유효하다면
            visited[nx][ny] = True  # 방문 처리 후
            backtrack(nx, ny, distance + 1)  # 재귀
            visited[nx][ny] = False  # 탐색 후 원상 복구


r, c, k = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]

# 위, 아래, 왼쪽, 오른쪽 좌표 이동을 반복문으로 쉽게 작성할 수 있도록 리스트 생성
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = 0
visited[r-1][0] = True  # 시작 좌표 방문 처리
backtrack(r-1, 0, 1)  # 시작 좌표 및 거리 1로 backtrack 함수 실행

print(result)  # 결과 출력
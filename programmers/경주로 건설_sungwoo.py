from collections import deque


def solution(board):

    def bfs():

        # 큐의 요소는 x 좌표, y 좌표, 직선 도로 형태(방향), 비용으로 구성됨 (도로 형태의 경우 0은 세로 직선 도로, 1는 가로 직선 도로, -1은 둘 다 가능한 시작 지점)
        q = deque([(0, 0, -1, 0)])
        dx = [1, -1, 0, 0]  # x 변위
        dy = [0, 0, 1, -1]  # y 변위
        dd = [0, 0, 1, 1]  # 변위에 따른 방향

        cost[0][0] = [0, 0]  # 시작 지점 비용 0으로 설정

        while q:
            x, y, d, c = q.popleft()  # x, y 좌표, 방향, 비용을 가져옴

            for i in range(4):  # 상하좌우 탐색
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:  # 유효한 위치라면
                    nc = c + (100 if d == dd[i] or d == -1 else 600)  # 비용 계산 (방향이 같은 경우 100, 달라지는 경우 600)

                    if nc < cost[nx][ny][dd[i]]:  # 새로 계산된 비용이 기존 같은 방향으로 계산된 비용보다 적다면  ( !!! 이 부분 <=로 할 경우 시간초과 발생하였음 !!! )
                        cost[nx][ny][dd[i]] = nc  # 비용 갱신 후
                        q.append((nx, ny, dd[i], nc))  # 큐에 삽입

    n = len(board)

    # 비용을 담는 3차원 리스트 생성 [x 좌표, y 좌표, 직선 도로 형태]로 구성됨 (직선 도로 형태, 즉 방향에 따라 비용을 나누어 관리해야 찐최적해를 구할 수 있음)
    cost = [[[float('inf'), float('inf')] for _ in range(n)] for _ in range(n)]
    bfs()  # BFS 수행

    return min(cost[n-1][n-1])

# 25번의 반례를 참고했으며,
# 단순히 최적의 cost를 매번 갱신하는 것이 아닌,
# 직선 도로 형태(방향)에 따라 cost를 관리해야 방향에 따라 달라질 수 있는 비용의 경우의 수를 모두 고려할 수 있음
from collections import deque

def bfs(dp, m, n, x, y, visited):

    # 인접한 좌표를 탐색하기 위한 dx, dy
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 큐 생성 후 시작 위치 초기화 및 방문 처리
    q = deque([(x,y)])
    visited[x][y] = True

    # BFS 수행
    while q:
        x, y = q.popleft()

        # 인접한 좌표 순회
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 유효한 위치이고, puddle이 아니라면 조건을 만족하며
            # 1. 해당 위치의 dp 값을 현재 위치의 dp 값에 누적함
            # 2. 방문하지 않은 곳이라면 추가적인 순회를 위해 큐에 추가하고 방문 처리함
            if 0 <= nx < m and 0 <= ny < n and dp[nx][ny] != -1:
                dp[x][y] += dp[nx][ny]

                if not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True

def solution(m, n, puddles):

    # DP를 활용한 풀이 (해당 좌표까지의 최단 거리 가짓 수를 저장)
    dp = [[0 for _ in range(n)] for _ in range(m)]
    visited = [[False for _ in range(n)] for _ in range(m)]

    # puddle은 DP 테이블 상에 -1로 저장하여 관리
    for i, j in puddles:
        dp[i-1][j-1] = -1

    # 시작 위치 DP 테이블 값 1로 시작하여 BFS 수행
    dp[0][0] = 1
    bfs(dp, m, n, 0, 0, visited)

    # 도착 위치의 DP 테이블 값을 리턴
    return dp[m-1][n-1] % 1000000007

print(solution(100, 100, []), 690285631)
print(solution(4, 4, [[1, 2], [3, 3]]), 4)
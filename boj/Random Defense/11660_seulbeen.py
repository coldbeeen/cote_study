import sys 
input = sys.stdin.readline

# 정답 풀이 
n, m = map(int,input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (n+1) for _ in range (n+1)]

# dp
for i in range (1, n+1) :
    for j in range (1, n+1) :
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + matrix[i-1][j-1]

# 원하는 구간 계산 
for _ in range (m):
    x1, y1, x2, y2 = map(int, input().split())

    ans = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]

    print(ans)


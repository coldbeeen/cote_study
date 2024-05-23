import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 인덱스 1부터로 사용하기 위해 패딩 붙여줌
graph = [[0 for _ in range(n)]] + [[0] + list(map(int, input().split())) for _ in range(n)]

# 행별로 합을 누적함
for i in range(1, n+1):
    for j in range(2, n+1):
        graph[i][j] += graph[i][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    result = 0
    # 행별로 누적된 합을 바탕으로 구간합을 구함
    for i in range(x1, x2+1):
        result += graph[i][y2] - graph[i][y1-1]

    print(result)
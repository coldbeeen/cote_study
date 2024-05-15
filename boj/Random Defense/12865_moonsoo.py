
N, K = map(int, input().split())

candidates = [(0,0)]
for _ in range(N):
    W, V = map(int, input().split())
    candidates.append((W, V))


dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for row in range(1, N+1):
    # 후보군을 하나씩 늘려가면서 최대를 찾는 과정
    w, v = candidates[row][0], candidates[row][1]

    for col in range(1, K+1):
        # 전 후보군까지에서 같은 무게일 때와 추가된 후보의 w를 뺀 가방에 v를 더한 것과 최대 비교
        dp[row][col] = max(dp[row - 1][col], dp[row - 1][col - w] + v if col-w>=0 else 0)


print(dp[N][K])
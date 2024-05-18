import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = [[0,0]] + [list(map(int, input().split())) for _ in range(n)]

# DP 테이블 생성 (배낭 최대 허용 무게와 몇 번째 아이템까지 고려했나를 기준으로 풀이)
dp = [[0 for _ in range(n+1)] for _ in range(k+1)]

for m in range(1, k+1):  # 배낭 최대 허용 무게 (max_weight)
    for c in range(1, n+1):  # c번째 아이템까지 고려하였을 때 (count)
        w, v = items[c][0], items[c][1]

        # 해당 아이템이 무게가 최대 허용 무게를 넘기지 않는다면
        # 해당 아이템의 무게를 뺀 c-1의 DP 값과 v를 더하여 이 값이 더 크다면 업데이트
        dp[m][c] = max(dp[m][c-1], v + dp[m-w][c-1] if w <= m else 0)

print(dp[k][n])
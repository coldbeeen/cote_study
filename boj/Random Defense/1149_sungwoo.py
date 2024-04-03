def rgb_idx_except(i):  # i(색)를 제외한 rgb 색 idx를 리턴
    rgb_idx = [0,1,2]
    rgb_idx.remove(i)
    return rgb_idx

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
dp = [[0,0,0] for _ in range(n)]  # dp 테이블 초기화
dp[0] = costs[0]  # dp 테이블 초깃값 설정

for i in range(1, n):
    for j in range(3):
        rgb1, rgb2 = rgb_idx_except(j)  # j 인덱스를 제외한 나머지 인덱스를 구함 (색이 같지 않도록)
        dp[i][j] = min(dp[i-1][rgb1], dp[i-1][rgb2]) + costs[i][j]  # 이전 행의 dp 테이블 인덱스를 참조해 최솟값 계산해나감

print(min(dp[n-1]))  # 마지막 행에서 최솟값 출력
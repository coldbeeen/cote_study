n, k = map(int, input().split())
coin = sorted([int(input()) for _ in range(n)])
dp = [0 for _ in range(k+1)]

# 전략
# 첫 dp 테이블은 첫 코인만 사용했을 때의 1~k를 만드는 경우의 수
# 다음에 갱신되는 dp 테이블은 첫 코인과 두 번째 코인을 사용했을 때의 1~k를 만드는 경우의 수
# j가 만들고자 하는 수일 때,
# 다음으로 업데이트되는 dp[j]는 dp[j - coin[i]] + (이전 조합의 값인) dp[j]로 구할 수 있음

dp[0] = 1  # 0열은 1로 초기화 (dp[i][j - coin[i]]를 활용하므로 코인 가치의 배수가 1씩 증가될 수 있도록 하기 위함)

for j in range(1, k+1):  # (최초) coin[0]을 활용해 1~k를 만드는 경우의 수 초기화
    if j % coin[0] == 0:
        dp[j] = 1

for i in range(1, n):  # 코인을 두 개 이상 활용 (~n번째 코인까지 활용했을 때의 값을 구함)
    for j in range(1, k+1):  # 1~k를 만드는 경우의 수
        if j - coin[i] >= 0:  # j가 coin[i]보다 같거나 큰 경우에만 dp[i][j - coin[i]] 값 활용
            dp[j] = dp[j - coin[i]] + dp[j]

print(dp[k])
t = int(input())

for _ in range(t):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0 for _ in range(n)] for _ in range(2)]  # DP 테이블 생성 (현재 위치까지의 최댓값을 저장할 것임)
    dp[0][0], dp[1][0] = stickers[0][0], stickers[1][0]  # 초깃값 설정

    # 현재 스티커를 선택할 수 있는 조건은, 1. 대각선 이전 열 스티커를 뗐거나, 2. 대각선 전전 열 스티커를 뗐거임
    # '대각선 이전 열'과 '대각선 전전 열' 중 더 큰 값을 선택해 현재 sticker를 이어서 선택
    for i in range(1, n):
        dp[0][i], dp[1][i] = (
            max(dp[1][i-1], dp[1][i-2]) + stickers[0][i],
            max(dp[0][i-1], dp[0][i-2]) + stickers[1][i]
        )

    print(max(dp[0][-1], dp[1][-1]))
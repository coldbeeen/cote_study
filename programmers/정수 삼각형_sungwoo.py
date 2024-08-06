def solution(triangle):

    # DP 테이블 생성
    dp = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    # 삼각형을 위에서부터 순회하며, 최댓값을 저장해나도록 함 (Bottom-Up 방식)
    # 점화식: dp[i][j] = max(dp[i-1], dp[j-1], dp[i-1][j]) + triangle[i][j]  (when j > 0)
    for i in range(1, len(triangle)):

        for j in range(i + 1):
            if j > 0:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            else:  # 왼쪽 위 값이 없는 경우
                dp[i][j] = dp[i-1][j] + triangle[i][j]

    # 삼각형 맨 아랫줄에서의 최댓값을 리턴
    return max(dp[len(triangle)-1])
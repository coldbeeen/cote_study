#구글링
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (N + 1) for _ in range(N + 1)] #누적합 저장을 위한 배열

for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + table[i - 1][j - 1]
        #table값 더해줄 때 인덱스 유의

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    
    result = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(result)
    #결과 = [x2, y2]까지의 전체 합 - (x1 직전까지의 row 합) - (y1 직전까지의 col 합) + 겹쳐서 추가 연산되었던 값
    
#2중 반복 사용하면 시간 초과 : O(n^2)은 안 됨
#그냥 표를 1차원으로 무너뜨려서 인덱스로 더해주면 되지 않나? ㄴㄴ 아님
#DP로 풀어야 할 것 같다 / 2차원 DP

#DP : 누적합
#특정 값 = 이전 row 값 + 이전 col 값 - (이전 row와 col이 겹치는 인덱스 값) + 현재 [row, col] 값
# 구간 합
